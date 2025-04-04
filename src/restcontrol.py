from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS
import logging
from typing import Optional, Dict, Any
from mktdata_finnhub import get_stock_price, StockPriceFetcher, FinnhubAPI

class StockPriceService:
    """Service layer for stock price operations."""
    def __init__(self, price_fetcher: Optional[StockPriceFetcher] = None):
        self.price_fetcher = price_fetcher or FinnhubAPI()
    
    def get_price(self, symbol: str) -> Optional[float]:
        """
        Get stock price for the given symbol.
        
        Args:
            symbol: Stock symbol
            
        Returns:
            Current stock price or None if error
        """
        return get_stock_price(symbol, self.price_fetcher)

class HealthCheckResource(Resource):
    """Resource for health check endpoint."""
    def get(self) -> Dict[str, str]:
        return {'status': 'healthy'}

class RootResource(Resource):
    """Resource for root endpoint."""
    def get(self) -> Dict[str, str]:
        return {'version': '1.0.1'}

class StockPriceResource(Resource):
    """Resource for stock price endpoint."""
    def __init__(self, price_service: Optional[StockPriceService] = None):
        self.price_service = price_service or StockPriceService()
    
    def get(self, symbol: str) -> Any:
        """
        Get stock price for the given symbol.
        
        Args:
            symbol: Stock symbol
            
        Returns:
            Price value or error message
        """
        price = self.price_service.get_price(symbol)
        if price is None:
            return {'error': f'Could not fetch price for {symbol}'}
        return price

class RESTController:
    """Main controller for REST API setup."""
    def __init__(self):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self._setup_cors()
        self._setup_logging()
        self._setup_routes()
    
    def _setup_cors(self) -> None:
        """Configure CORS settings."""
        CORS(self.app, resources={r"*": {"origins": "*"}})
    
    def _setup_logging(self) -> None:
        """Configure logging settings."""
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.INFO
        )
    
    def _setup_routes(self) -> None:
        """Setup API routes."""
        self.api.add_resource(RootResource, '/')
        self.api.add_resource(HealthCheckResource, '/health')
        self.api.add_resource(StockPriceResource, '/price/<string:symbol>')
    
    def run(self, host: str = "0.0.0.0", port: int = 80, debug: bool = True) -> None:
        """Run the Flask application."""
        self.app.run(host=host, port=port, debug=debug, use_reloader=False)

if __name__ == '__main__':
    controller = RESTController()
    controller.run()

