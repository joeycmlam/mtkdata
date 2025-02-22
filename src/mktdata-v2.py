import yfinance as yf
from datetime import datetime, timedelta
import logging


class StockPriceGetter:
    def __init__(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def get_latest_price(self, stock_code):
        try:
            end_date = datetime.now().strftime("%Y-%m-%d")
            start_date = (datetime.now() - timedelta(days=5)).strftime("%Y-%m-%d")

            data = yf.download(stock_code, start=start_date, end=end_date)

            if data.empty:
                self.logger.info(f"No data available for {stock_code}")
                return None

            latest_price = data['Close'].iloc[-1]
            self.logger.info(f"Latest closing price for {stock_code}: {latest_price}")
            return latest_price
        except Exception as e:
            self.logger.error(f"Error fetching price for {stock_code}: {str(e)}")
            return None

    def get_historical_prices(self, stock_code, start_date, end_date):
        try:
            data = yf.download(stock_code, start=start_date, end=end_date)

            if data.empty:
                self.logger.info(f"No historical data available for {stock_code}")
                return None

            prices = data['Close'].to_dict()
            self.logger.info(f"Retrieved historical prices for {stock_code}")
            return prices
        except Exception as e:
            self.logger.error(f"Error fetching historical prices for {stock_code}: {str(e)}")
            return None


if __name__ == '__main__':
    # Create an instance of the class
    price_getter = StockPriceGetter()

    # Get the latest price for a stock
    apple_price = price_getter.get_latest_price("AAPL")
    print(f"Latest Apple stock price: ${apple_price}")

    # # Get historical prices
    # start_date = "2025-01-01"
    # end_date = "2025-02-22"
    # apple_historical = price_getter.get_historical_prices("AAPL", start_date, end_date)
    # print("Historical Apple stock prices:", apple_historical)
