import requests
import logging
from datetime import datetime
from config_reader import ConfigReader

class FinnhubAPI:
    def __init__(self, config_reader=None):
        self.config_reader = config_reader or ConfigReader()
        self.api_key = self.config_reader.get_api_key('FINNHUB')
        self.base_url = 'https://finnhub.io/api/v1'
        self.logger = logging.getLogger(__name__)

    def get_stock_price(self, symbol):
        """
        Fetch real-time stock price using Finnhub API
        
        Args:
            symbol (str): Stock symbol (e.g., 'AAPL' for Apple)
            
        Returns:
            dict: Stock price information including current price and change
        """
        try:
            # Endpoint for real-time quote
            endpoint = f"{self.base_url}/quote"
            
            # Parameters for the API call
            params = {
                'symbol': symbol,
                'token': self.api_key
            }
            
            # Make the API request
            response = requests.get(endpoint, params=params)
            
            # Check if request was successful
            if response.status_code == 200:
                data = response.json()
                
                # Check if we got valid data
                if data and 'c' in data:
                    return {
                        'symbol': symbol,
                        'price': data['c'],
                        'change': data['d'],
                        'percent_change': data['dp'],
                        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    }
                else:
                    self.logger.error(f"No data available for symbol {symbol}")
                    return None
            else:
                self.logger.error(f"API returned status code {response.status_code}")
                return None
                
        except requests.exceptions.RequestException as e:
            self.logger.error(f"Error fetching data: {str(e)}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error: {str(e)}")
            return None

# Create a singleton instance
finnhub_api = FinnhubAPI()

def getTodayPrice(symbol):
    """
    Get today's stock price for the given symbol
    
    Args:
        symbol (str): Stock symbol
        
    Returns:
        dict: Stock price information or None if error
    """
    return finnhub_api.get_stock_price(symbol)

if __name__ == '__main__':
    symbol = 'AAPL'
    result = getTodayPrice(symbol) 
    print(result)