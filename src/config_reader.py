import json
import os
import logging

class ConfigReader:
    def __init__(self, config_path=None):
        self.logger = logging.getLogger(__name__)
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        self.config_path = config_path
        self.config = self._load_config()

    def _load_config(self):
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

    def get_api_key(self, service):
        try:
            return self.config[service]['API_KEY']
        except KeyError:
            self.logger.error(f"API key not found for service {service}")
            return None 