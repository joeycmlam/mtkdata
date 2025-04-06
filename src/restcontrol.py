from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import logging
from typing import Dict, Any
from mktdata_finnhub import get_stock_price

class RestControl:
    """REST API controller for stock price data."""
    
    def __init__(self):
        self.app = Flask(__name__)
        self._setup_cors()
        self.api = Api(self.app)
        self._setup_routes()
        self._setup_logging()
    
    def _setup_cors(self) -> None:
        """Configure CORS settings."""
        CORS(self.app, resources={r"*": {"origins": "*"}})
    
    def _setup_routes(self) -> None:
        """Register API routes."""
        self.api.add_resource(RootResource, '/')
        self.api.add_resource(HealthCheckResource, '/test')
        self.api.add_resource(StockPriceResource, '/price/<string:stockcode>')
    
    def _setup_logging(self) -> None:
        """Configure logging settings."""
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.INFO
        )
    
    def run(self, host: str = '0.0.0.0', port: int = 80, debug: bool = True) -> None:
        """Run the Flask application.
        
        Args:
            host: Host to bind to.
            port: Port to listen on.
            debug: Whether to run in debug mode.
        """
        self.app.run(host=host, port=port, debug=debug, use_reloader=False)


class RootResource(Resource):
    """Root endpoint resource."""
    
    def get(self) -> Dict[str, str]:
        """Handle GET requests to the root endpoint.
        
        Returns:
            Dictionary containing API version information.
        """
        return {'src': 'version 1.0.1'}


class HealthCheckResource(Resource):
    """Health check endpoint resource."""
    
    def get(self) -> Dict[str, str]:
        """Handle GET requests to the health check endpoint.
        
        Returns:
            Dictionary containing health check status.
        """
        return {'status': 'healthy'}


class StockPriceResource(Resource):
    """Stock price endpoint resource."""
    
    def get(self, stockcode: str) -> Dict[str, Any]:
        """Handle GET requests for stock price data.
        
        Args:
            stockcode: The stock symbol to fetch price for.
            
        Returns:
            Dictionary containing stock price data.
        """
        try:
            price_data = get_stock_price(stockcode)
            if not price_data:
                return {'error': f'No price data available for {stockcode}'}, 404
            return price_data
        except Exception as e:
            logging.error(f"Error fetching price for {stockcode}: {str(e)}")
            return {'error': 'Internal server error'}, 500


if __name__ == '__main__':
    controller = RestControl()
    controller.run()
