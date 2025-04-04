import requests

if __name__ == "__main__":
    API_KEY = "bfb97c479eac18798eb51bfd8f73d1dd"  # Get from marketstack.com
    symbol = "0700.HK"

    url = f"http://api.marketstack.com/v1/tickers/{symbol}/eod/latest?access_key={API_KEY}"
    data = requests.get(url).json()["data"]["eod"][0]
    print({
        "price": data["close"],
        "currency": "HKD",
        "date": data["date"]
    })