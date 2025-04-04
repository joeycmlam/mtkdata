import requests
import logging
from datetime import datetime
from typing import Optional, Dict, Any, Protocol
from config_reader import ConfigReader

class StockPriceData:
    """Data class for stock price information."""
    def __init__(self, price: float, timestamp: str):
        self.price = price
        self.timestamp = timestamp

class StockPriceFetcher(Protocol):
    """Interface for fetching stock prices."""
    def get_stock_price(self, symbol: str) -> Optional[StockPriceData]:
        """Fetch stock price for given symbol."""
        ...

class FinnhubClient:
    """Handles direct communication with Finnhub API."""
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url
        self.logger = logging.getLogger(__name__)

    def _build_endpoint(self, path: str) -> str:
        """Build the full API endpoint URL."""
        return f"{self.base_url}/{path}"

    def _make_request(self, endpoint: str, params: Dict[str, str]) -> Optional[Dict[str, Any]]:
        """Make an HTTP request to the API."""
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            return None

class FinnhubAPI(StockPriceFetcher):
    """Client for interacting with the Finnhub API."""
    section_name: str = 'FINNHUB'
    
    def __init__(self, config_reader: Optional[ConfigReader] = None):
        self.config_reader = config_reader or ConfigReader()
        self.api_key = self.config_reader.get_api_key(self.section_name)
        self.base_url = self.config_reader.get_base_url(self.section_name)
        self.client = FinnhubClient(self.api_key, self.base_url)

    def get_stock_price(self, symbol: str) -> Optional[StockPriceData]:
        """
        Fetch real-time stock price using Finnhub API.
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL' for Apple)
            
        Returns:
            Stock price data or None if error
        """
        endpoint = self.client._build_endpoint('quote')
        params = {
            'symbol': symbol,
            'token': self.api_key
        }
        
        data = self.client._make_request(endpoint, params)
        if not data or 'c' not in data:
            return None
            
        return StockPriceData(
            price=data['c'],
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

def get_stock_price(symbol: str, fetcher: Optional[StockPriceFetcher] = None) -> Optional[float]:
    """
    Get stock price for the given symbol.
    
    Args:
        symbol: Stock symbol
        fetcher: Optional StockPriceFetcher instance
        
    Returns:
        Current stock price or None if error
    """
    api = fetcher or FinnhubAPI()
    result = api.get_stock_price(symbol)
    return result.price if result else None

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python mktdata_finnhub.py <symbol>")
        sys.exit(1)
        
    symbol = sys.argv[1]
    result = get_stock_price(symbol)
    print(result)