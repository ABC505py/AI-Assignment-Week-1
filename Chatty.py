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


def get_user_query():
    return input("Ask me about crypto investment advice: ").lower()


def advise_on_profitability():
    for coin, data in crypto_db.items():
        if data["price_trend"] == "rising" and data["market_cap"] == "high":
            return f"📈 Consider investing in {coin}! It's rising and has a high market cap."
    return "No coin currently meets the top profitability criteria."


def advise_on_sustainability():
    sustainable_coins = [coin for coin in crypto_db if crypto_db[coin]["energy_use"] == "low" and crypto_db[coin]["sustainability_score"] > 0.7]
    if sustainable_coins:
        return f"🌱 Consider investing in {sustainable_coins[0]}! It’s eco-friendly and viable long-term."
    return "No coin currently meets the top sustainability criteria."


def advise_on_trending():
    trending = [coin for coin in crypto_db if crypto_db[coin]["price_trend"] == "rising"]
    return f"Trending up: {', '.join(trending)} 📊"


def chatbot():
    print("Welcome to the Crypto Investment Advisor Bot! 🤖")
    while True:
        query = get_user_query()
        if "trend" in query or "trending" in query:
            print(advise_on_trending())
        elif "sustainable" in query:
            print(advise_on_sustainability())
        elif "profitable" in query or "profit" in query:
            print(advise_on_profitability())
        elif "exit" in query or "quit" in query:
            print("Goodbye and happy investing! 🚀")
            break
        else:
            print("Sorry, I didn't understand that. Try asking about trends, profitability, or sustainability.")


if __name__ == "__main__":
    chatbot()
