import json
import os
import logging
from typing import Optional, Dict, Any

class ConfigReader:
    """Handles reading and accessing configuration from JSON files."""
    
    def __init__(self, config_file: Optional[str] = None):
        self.logger = logging.getLogger(__name__)
        self.config_path = self._get_config_path(config_file)
        self.config = self._load_config()

    def _get_config_path(self, config_file: Optional[str]) -> str:
        """Get the full path to the config file."""
        if config_file is None:
            config_file = 'config.json'
        return os.path.join(os.path.dirname(__file__), config_file)

    def _load_config(self) -> Dict[str, Any]:
        """Load and validate the configuration file."""
        try:
            with open(self.config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"Config file not found at {self.config_path}")
            raise
        except json.JSONDecodeError:
            self.logger.error(f"Invalid JSON in config file {self.config_path}")
            raise
        except Exception as e:
            self.logger.error(f"Error loading config: {str(e)}")
            raise

    def get_service_config(self, service: str) -> Dict[str, str]:
        """Get all configuration for a specific service."""
        try:
            return self.config[service]
        except KeyError:
            self.logger.error(f"Configuration not found for service {service}")
            return {}

    def get_api_key(self, service: str) -> Optional[str]:
        """Get the API key for a specific service."""
        service_config = self.get_service_config(service)
        return service_config.get('API_KEY')

    def get_base_url(self, service: str) -> Optional[str]:
        """Get the base URL for a specific service."""
        service_config = self.get_service_config(service)
        return service_config.get('BASE_URL') 