from alpha_vantage.timeseries import TimeSeries
import pandas as pd

# Replace with your Alpha Vantage API key
API_KEY = "API_KEY"


def get_stock_price(ticker):
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        data, meta_data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='compact')

        if not data.empty:
            latest_price = data['4. close'].iloc[-1]
            print(f"The latest closing price for {ticker} is: ${latest_price:.2f}")
            return latest_price
        else:
            print(f"No data found for the ticker: {ticker}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    get_stock_price('C')
