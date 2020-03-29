import yfinance as yf
from datetime import date

#class mktPrice:


    #def __init__(self):
        # body of the constructor


def getTodayPrice(stockCode):
    latestDate = date.today().strftime("%Y-%m-%d")
    price = getPrice(stockCode, latestDate, latestDate)


    return price

def getCurrentStockInfo(stockCode):
    latestDate = date.today().strftime("%Y-%m-%d")
    values = getStockInfo(stockCode, latestDate, latestDate)
    return values

def getStockInfo(stockCode, fromDate, toDate):
    listStockCodes = "T " + stockCode
    data = yf.download(listStockCodes, start=fromDate, end=toDate, group_by="ticker")

    values = data[stockCode]['Close']

    return values

def getPrice(stockCode, fromDate, toDate):
    closingPrice = 0

    values = getStockInfo(stockCode, fromDate, toDate)
    #pprint.pprint(values)

    price_list = values.tolist()

    closingPrice = price_list[0]

    return closingPrice
