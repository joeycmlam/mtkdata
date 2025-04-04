from typing import Optional, Dict, Any
from src.mktdata_finnhub import StockPriceFetcher, StockPriceData

class MockFinnhubAPI(StockPriceFetcher):
    """Mock implementation of Finnhub API for testing."""
    
    def __init__(self):
        self.mock_prices: Dict[str, float] = {
            'AAPL': 150.0,
            'GOOGL': 2800.0,
            'MSFT': 300.0
        }
    
    def get_stock_price(self, symbol: str) -> Optional[StockPriceData]:
        """Mock implementation of get_stock_price."""
        if not symbol or symbol not in self.mock_prices:
            return None
            
        return StockPriceData(
            price=self.mock_prices[symbol],
            timestamp='2023-01-01 12:00:00'
        ) 