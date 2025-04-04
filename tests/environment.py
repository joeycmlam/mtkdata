from behave import fixture, use_fixture
from src.mktdata_finnhub import FinnhubAPI
from tests.mocks.mock_finnhub import MockFinnhubAPI

@fixture
def mock_finnhub(context):
    """Fixture to provide a mock Finnhub API instance."""
    context.mock_api = MockFinnhubAPI()
    return context.mock_api

def before_scenario(context, scenario):
    """Setup before each scenario."""
    use_fixture(mock_finnhub, context) 