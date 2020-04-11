import pprint

import yfinance as yf
from datetime import datetime, timedelta

#class mktPrice:


    #def __init__(self):
        # body of the constructor


def getTodayPrice(stockCode):
    closingPrice = 0

    latestDate = datetime.now().strftime("%Y-%m-%d")
    fromDate = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

    result = getStockInfo(stockCode, fromDate, latestDate)

    price_list = result['Close']

    num_record = len(price_list)
    if num_record == 0:
        pprint.pprint("price_list[] is empty")
    else:
        closingPrice = price_list[num_record-1]

    return closingPrice



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
    #values = data[stockCode]['Close']

    return data[stockCode]

def getPrice(stockCode, fromDate, toDate):
    closingPrice = 0


    values = getStockInfo(stockCode, fromDate, toDate)
    pprint.pprint(values)

    price_list = values

    if price_list == []:
        pprint.pprint("price_list[] is empty")
    else:
        closingPrice = price_list[len(price_list)-1]

    return closingPrice


def getPriceInfo(stockCode, fromDate, toDate):
    closingPrice = 0


    values = getStockInfo(stockCode, fromDate, toDate)
    pprint.pprint(values)

    #price_list = values.tolist()

    result = values['Close'].tolist()
    return result


