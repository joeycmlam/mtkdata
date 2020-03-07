import yfinance as yf
from datetime import date

#class mktPrice:


    #def __init__(self):
        # body of the constructor


def getTodayPrice(stockCode):
    latestDate = date.today().strftime("%Y-%m-%d")
    price = getPrice(stockCode, latestDate, latestDate)


    return price

def getPrice(stockCode, fromDate, toDate):
    closingPrice = 0

    listStockCodes = "PFF " + stockCode
    data = yf.download(listStockCodes, start=fromDate, end=toDate, group_by="ticker")

    values = data[stockCode]['Close']

    #pprint.pprint(values)

    price_list = values.tolist()

    closingPrice = price_list[0]

    return closingPrice
