import yfinance as yf
import pprint
from datetime import date

def getTodayPrice(stockCode):
    today = date.today()
    latestDate = today.strftime("%Y-%m-%d")

    price = getPrice(stockCode, latestDate, latestDate)

    return price

def getPrice(stockCode, fromDate, toDate):
    closingPrice = 0

    listStockCodes = "0001.HK " + stockCode
    data = yf.download(listStockCodes, start=fromDate, end=toDate, group_by="ticker")

    values = data[stockCode]['Close']

    pprint.pprint(values)

    price_list = values.tolist()

    closingPrice = price_list[0]



    return closingPrice


