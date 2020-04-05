import pprint

import yfinance as yf
from datetime import datetime, timedelta

#class mktPrice:


    #def __init__(self):
        # body of the constructor


def getTodayPrice(stockCode):
    latestDate = datetime.now().strftime("%Y-%m-%d")
    fromDate = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')
    price = getPrice(stockCode, fromDate, latestDate)


    return price

def getCurrentStockInfo(stockCode):
    latestDate = datetime.now().strftime("%Y-%m-%d")
    fromDate = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')
    values = getStockInfo(stockCode, fromDate, latestDate)
    return values

def getStockInfo(stockCode, fromDate, toDate):
    listStockCodes = "T " + stockCode

    pprint.pprint("getStockInfo: stockcode = {0} {1} {2}".format(listStockCodes, fromDate, toDate))
    data = yf.download(listStockCodes, start=fromDate, end=toDate, group_by="ticker")

    pprint.pprint("getStockInfo: data {0}".format(data))
    values = data[stockCode]['Close']

    return values

def getPrice(stockCode, fromDate, toDate):
    closingPrice = 0


    values = getStockInfo(stockCode, fromDate, toDate)
    pprint.pprint(values)

    price_list = values.tolist()

    if price_list == []:
        pprint.pprint("price_list[] is empty")
    else:
        closingPrice = price_list[len(price_list)-1]

    return closingPrice
