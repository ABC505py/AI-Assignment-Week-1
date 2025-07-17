# AI-Assignment-Week-1
# 🤖 Crypto Investment Advisor Bot

## 📘 Description

The **Crypto Investment Advisor Bot** is a simple, rule-based Python chatbot that provides basic investment advice on cryptocurrencies. It analyzes a small dataset of coins and gives guidance based on:

- 📈 **Profitability** (e.g., price trends and market capitalization)
- 🌱 **Sustainability** (e.g., energy efficiency and viability score)

This chatbot uses plain `if-else` logic and runs entirely in the terminal. It's ideal for beginners learning Python, logic-based AI, or cryptocurrency fundamentals.

---

## 🧠 How It Works

The bot uses a small hard-coded dataset of cryptocurrencies:

```python
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}
