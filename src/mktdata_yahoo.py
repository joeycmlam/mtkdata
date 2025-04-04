import yfinance as yf

def get_hk_stock(symbol):
    stock = yf.Ticker(f"{symbol}.HK")
    data = stock.history(period="1d")
    return {
        "price": data["Close"].iloc[-1],
        "currency": "HKD",
        "time": data.index[-1].strftime("%Y-%m-%d %H:%M:%S")
    }

if __name__ == "__main__":
    # Example: Tencent (0700.HK)
    print(get_hk_stock("0700"))