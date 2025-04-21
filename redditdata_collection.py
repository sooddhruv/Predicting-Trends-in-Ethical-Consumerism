#pip install praw pandas
# Install necessary libraries
#!pip install praw pandas regex

import praw
import pandas as pd
import re
from datetime import datetime, timedelta
import time
from prawcore.exceptions import TooManyRequests, ResponseException

# Define the companies and keywords
keywords = [
    "sustainability", "sustainable", "eco-friendly", "consumerism",
    "environmental", "climate change", "carbon footprint",
    "renewable", "ESG", "clean energy", "recycling",
    "circular economy", "biodegradable", "emissions",
    "social responsibility", "renewable energy", "zero waste"
]

companies = [
    "Apple", "Microsoft", "Amazon", "Google", "Meta", "Tesla",
    "Nike", "Adidas", "Lululemon", "H&M", "Zara",
    "Under Armour", "Walmart", "Target", "Coca-Cola", "PepsiCo"
]

# Enhanced function to fetch data
def fetch_reddit_data(subreddit_name, keywords, companies, start_date, end_date, max_retries=3, delay=60):
    data = []
    reddit = praw.Reddit(
        client_id="VJOMEo6dRSrLiSN5bI_5NQ",
        client_secret="hNsJtn-azHuFrwQ_Cn8RPZWjosTZAQ",
        user_agent="EthicalConsumerApp/1.0"
    )
    subreddit = reddit.subreddit(subreddit_name)

    # Combine keywords and companies for broader search
    search_terms = keywords + companies

    for term in search_terms:
        print(f"Searching for '{term}' in r/{subreddit_name}")
        retries = 0
        while retries < max_retries:
            try:
                # Search for posts
                for submission in subreddit.search(term, sort="new", time_filter="year"):
                    # Check post date range
                    post_date = datetime.fromtimestamp(submission.created_utc)
                    if start_date <= post_date <= end_date:
                        # Scrape the post itself
                        for company in companies:
                            if company.lower() in submission.title.lower() or company.lower() in submission.selftext.lower():
                                data.append({
                                    "keyword": term,
                                    "company_name": company,
                                    "post_title": submission.title,
                                    "post_id": submission.id,
                                    "post_body": submission.selftext,
                                    "post_score": submission.score,
                                    "post_comments": submission.num_comments,
                                    "timestamp": post_date
                                })

                        # Scrape comments and sub-comments
                        submission.comments.replace_more(limit=None)
                        for comment in submission.comments.list():
                            # Check if the comment body mentions both keywords and companies
                            for company in companies:
                                if any(kw.lower() in comment.body.lower() for kw in keywords) and company.lower() in comment.body.lower():
                                    data.append({
                                        "keyword": term,
                                        "company_name": company,
                                        "post_title": submission.title,
                                        "post_id": submission.id,
                                        "comment_id": comment.id,
                                        "comment_body": comment.body,
                                        "comment_score": comment.score,
                                        "timestamp": datetime.fromtimestamp(comment.created_utc)
                                    })

                break  # If successful, break out of the retry loop
            except (TooManyRequests, ResponseException) as e:
                retries += 1
                print(f"Rate limit hit. Retrying in {delay} seconds... (Attempt {retries}/{max_retries})")
                time.sleep(delay)
        else:
            print(f"Failed to fetch data for term '{term}' after {max_retries} attempts.")

        # Small delay between terms to avoid rate limits
        time.sleep(3)

    return pd.DataFrame(data)

# Set date range for past year
end_date = datetime.now()
start_date = end_date - timedelta(days=100)

# Fetch data from r/wallstreetbets
subreddit_name = "wallstreetbets"
sustainability_data = fetch_reddit_data(subreddit_name, keywords, companies, start_date, end_date)

# Save results to CSV
csv_filename = f"{subreddit_name}_sustainability_data_with_companies.csv"
sustainability_data.to_csv(csv_filename, index=False)

print(f"Data collection complete. {len(sustainability_data)} items saved to {csv_filename}")
