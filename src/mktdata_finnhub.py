import requests
import logging
from datetime import datetime
from typing import Optional, Dict, Any
from config_reader import ConfigReader

class StockPriceResponse:
    """Data class for stock price response."""
    
    def __init__(self, symbol: str, price: float, change: float, 
                 percent_change: float, timestamp: str):
        self.symbol = symbol
        self.price = price
        self.change = change
        self.percent_change = percent_change
        self.timestamp = timestamp

    def to_dict(self) -> Dict[str, Any]:
        """Convert the response to a dictionary."""
        return {
            'symbol': self.symbol,
            'price': self.price,
            'change': self.change,
            'percent_change': self.percent_change,
            'timestamp': self.timestamp
        }

class FinnhubAPI:
    """Client for interacting with the Finnhub API."""
    section_name: str = 'FINNHUB'
    
    def __init__(self, config_reader: Optional[ConfigReader] = None):
        self.config_reader = config_reader or ConfigReader()
        self.api_key = self.config_reader.get_api_key(self.section_name)
        self.base_url = self.config_reader.get_base_url(self.section_name)
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

    def _parse_response(self, symbol: str, data: Dict[str, Any]) -> Optional[StockPriceResponse]:
        """Parse the API response into a StockPriceResponse object."""
        if not data or 'c' not in data:
            self.logger.error(f"Invalid response data for symbol {symbol}")
            return None

        return StockPriceResponse(
            symbol=symbol,
            price=data['c'],
            change=data['d'],
            percent_change=data['dp'],
            timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        )

    def get_stock_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        """
        Fetch real-time stock price using Finnhub API.
        
        Args:
            symbol: Stock symbol (e.g., 'AAPL' for Apple)
            
        Returns:
            Stock price information or None if error
        """
        endpoint = self._build_endpoint('quote')
        params = {
            'symbol': symbol,
            'token': self.api_key
        }
        
        data = self._make_request(endpoint, params)
        if not data:
            return None
            
        response = self._parse_response(symbol, data)
        return response.to_dict() if response else None



def getTodayPrice(symbol: str) -> Optional[Dict[str, Any]]:
    """
    Get today's stock price for the given symbol.
    
    Args:
        symbol: Stock symbol
        
    Returns:
        Stock price information or None if error
    """
    # Create a singleton instance
    finnhub_api = FinnhubAPI()
    return finnhub_api.get_stock_price(symbol)

if __name__ == '__main__':
    symbol = 'AAPL'
    result = getTodayPrice(symbol)
    print(result)