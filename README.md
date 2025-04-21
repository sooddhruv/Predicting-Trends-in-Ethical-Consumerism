# 🌱 Predicting Trends in Ethical Consumerism

This project investigates the relationship between **public sentiment on corporate sustainability** and **stock price movements**, using Reddit discussions and stock market data. By analyzing posts from r/wallstreetbets and applying sentiment analysis tools like VADER and TextBlob, we aim to uncover whether positive or negative discussions about sustainability efforts influence a company’s stock performance.

## 👨‍💻 Contributors

- **Dhruv Sood**  
- **Saurav Premkumar**  
- **Rishabh Parakh**

## 📌 Objective

To determine if **positive public sentiment** toward a company's sustainability practices leads to **better stock performance**.

---

## 🧠 Methodology

1. **Data Collection**
   - Scraped Reddit comments from r/wallstreetbets using the PRAW API  
   - Filtered posts using sustainability-related keywords and company names

2. **Sentiment Analysis**
   - Combined **VADER** (70% weight) and **TextBlob** (30% weight) scores  
   - Weekly sentiment aggregation

3. **Stock Price Data**
   - Pulled from `yfinance` for relevant companies  
   - Merged with sentiment scores to analyze correlation

4. **Correlation Analysis**
   - Focused on companies like Microsoft, NVIDIA, Meta, and Google  
   - Explored positive/negative sentiment trends and their market impact

---

## 📊 Key Findings

| Company     | Correlation (Sentiment ↔ Stock) | Insight                                          |
|-------------|----------------------------------|--------------------------------------------------|
| Microsoft   | +0.55                            | Positive sentiment aligns with price growth     |
| NVIDIA      | -0.07                            | Weak negative relationship                      |
| Google      | -0.21                            | Negative sentiment associated with price drops  |
| Meta        | +0.15                            | Almost no relationship                          |

---

## 🔍 Why VADER & TextBlob?

- **VADER**: Excellent for social media, handles slang, emojis, and sarcasm well  
- **TextBlob**: Adds an additional layer for nuanced analysis  
- ✅ Combined: Creates a robust, interpretable, and computationally efficient sentiment pipeline

---

## 🚧 Challenges

- Limited access to ESG scores and structured financial data  
- Scraping unstructured Reddit data at scale  
- Aligning time windows between sentiment and market data  

---

## 🔮 Future Work

- Integrate **BERT/RoBERTa** for advanced sentiment analysis  
- Expand to more industries and companies  
- Incorporate **event-driven** analysis and time-lagged sentiment effects  
- Build predictive ML models (e.g., Random Forests, XGBoost)  
- Develop interactive dashboards for stakeholders  

---
---

## 📈 Example Visualization

<img width="932" alt="Screenshot 2025-04-21 at 5 14 14 PM" src="https://github.com/user-attachments/assets/5cfcd452-9fd1-460d-a070-a0ec4d7ccc0d" />





<img width="920" alt="Screenshot 2025-04-21 at 5 14 42 PM" src="https://github.com/user-attachments/assets/c264107d-771a-474f-b5d2-4f734b22c4b2" />

---

## 📬 Contact

Feel free to reach out via [LinkedIn](https://www.linkedin.com/in/sooddhruv2/)!

---
