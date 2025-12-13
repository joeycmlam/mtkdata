from typing import Optional, Dict, Any
from price_service import PriceService
from mktdata_finnhub import get_stock_price
from logger_config import logger


class FinnhubPriceService(PriceService):
    """Finnhub implementation of the price service."""

    def get_stock_price(self, symbol: str) -> Optional[Dict[str, Any]]:
        """Get stock price data from Finnhub.
        
        Args:
            symbol: The stock symbol to fetch price for.
            
        Returns:
            Dictionary containing price data or None if not available.
        """
        try:
            logger.debug(f"Fetching price from Finnhub for symbol: {symbol}")
            price_data = get_stock_price(symbol)
            if price_data:
                logger.debug(f"Successfully fetched price data from Finnhub for {symbol}")
            else:
                logger.warning(f"No price data returned from Finnhub for {symbol}")
            return price_data
        except Exception as e:
            logger.error(f"Error fetching price from Finnhub for {symbol}: {str(e)}", exc_info=True)
            return None
