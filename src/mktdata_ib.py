from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
import threading
import time
import sys

# Create a class that inherits from EWrapper and EClient
class IBapi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)
        self.data = {}  # Store the stock data here

    # Callback for real-time market data
    def tickPrice(self, reqId, tickType, price, attrib):
        if tickType == 4:  # 4 is the tick type for the last price
            self.data['last_price'] = price
            print(f"Last Price: {price}")

    # Callback for errors
    def error(self, reqId, errorCode, errorString):
        print(f"Error: {errorCode} - {errorString}")

def run_loop(app):
    app.run()

# Function to create a stock contract
def create_contract(symbol):
    contract = Contract()
    contract.symbol = symbol  # Stock ticker symbol (e.g., AAPL)
    contract.secType = "STK"  # Security type (STK for stocks)
    contract.exchange = "SMART"  # Use SMART routing
    contract.currency = "USD"  # Currency
    return contract

# Main function
def get_stock_price(symbol):
    app = IBapi()
    app.connect("127.0.0.1", 7497, clientId=1)  # Connect to TWS (port 7496) or IB Gateway (port 4001)

    # Start the socket in a thread
    api_thread = threading.Thread(target=run_loop, args=(app,), daemon=True)
    api_thread.start()

    time.sleep(1)  # Wait for the connection to establish

    # Create a contract for the stock
    contract = create_contract(symbol)

    # Request market data
    app.reqMktData(1, contract, "", False, False, None)

    time.sleep(5)  # Wait for the data to come in

    # Disconnect
    app.disconnect()

    # Return the last price
    return app.data.get('last_price', None)

if __name__ == "__main__":
    # symbol = input("Enter the stock ticker symbol (e.g., AAPL): ").strip().upper()
    symbol = "C"
    price = get_stock_price(symbol)
    if price:
        print(f"The latest price for {symbol} is: {price}")
    else:
        print(f"Could not retrieve the price for {symbol}.")
    sys.exit(0)