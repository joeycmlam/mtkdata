import requests

if __name__ == "__main__":
    API_KEY = "azZCBD5o92bktowVYGOIgZXjenFGDs1h"  # Get from financialmodelingprep.com
    symbol = "0700.HK"

    url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"
    data = requests.get(url).json()[0]
    print({
        "price": data["price"],
        "currency": "HKD",
        "time": data["timestamp"]
    })