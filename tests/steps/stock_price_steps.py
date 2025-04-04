from behave import given, when, then
from src.mktdata_finnhub import get_stock_price
from typing import Optional


class StockPriceContext:
    def __init__(self):
        self.symbol: Optional[str] = None
        self.price: Optional[float] = None
        self.error: Optional[str] = None


@given('I have a stock symbol "{symbol}"')
def step_given_valid_symbol(context, symbol):
    context.stock_price = StockPriceContext()
    context.stock_price.symbol = symbol
    context.stock_price.price = None  # Initialize price as None


@given('I have an empty stock symbol')
def step_given_empty_symbol(context):
    context.stock_price = StockPriceContext()
    context.stock_price.symbol = ""


@when('I request the stock price')
def step_when_request_price(context):
    try:
        context.stock_price.price = get_stock_price(context.stock_price.symbol)
    except Exception as e:
        context.stock_price.error = str(e)


@then('I should receive a price value of {expected_price:g}')
def step_then_receive_specific_price(context, expected_price):
    assert context.stock_price.price is not None, "Expected a valid price value"
    # assert isinstance(context.stock_price.price, float), "Price should be a float"
    assert context.stock_price.price == expected_price, f"Expected price {expected_price}, got {context.stock_price.price}"

