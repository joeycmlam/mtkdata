from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from datetime import datetime, timedelta
import logging


class AlphaStockPriceGetter:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_latest_price(self, ticker):

        try:
            API_KEY = "API_KEY"
            ts = TimeSeries(key=API_KEY, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=ticker, interval='1min', outputsize='compact')

            if not data.empty:
                latest_price = data['4. close'].iloc[-1]
                self.logger.info(f"Latest closing price for {ticker}: {latest_price}")
                return latest_price
            else:
                self.logger.info(f"No data available for {ticker}")
                return 0
        except Exception as e:
            self.logger.error(f"Error fetching price for {ticker}: {str(e)}")
            return None


if __name__ == '__main__':
    # Create an instance of the class
    price_getter = AlphaStockPriceGetter()

    # Get the latest price for a stock
    apple_price = price_getter.get_latest_price("AAPL")
    print(f"Latest Apple stock price: ${apple_price}")

    # # Get historical prices
    # start_date = "2025-01-01"
    # end_date = "2025-02-22"
    # apple_historical = price_getter.get_historical_prices("AAPL", start_date, end_date)
    # print("Historical Apple stock prices:", apple_historical)
