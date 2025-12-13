from typing import Optional, Dict, Any
from abc import ABC, abstractmethod

class PriceService(ABC):
    """Interface for price data services."""
    
    @abstractmethod
    def get_stock_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Get stock price data for a given symbol.
        
        Args:
            symbol: The stock symbol to fetch price for.
            
        Returns:
            Dictionary containing price data or None if not available.
        """
        pass 