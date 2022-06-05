import pprint
import yfinance as yf
from datetime import datetime, timedelta
import json
import logging
import numpy

def getTodayPrice(stockCode):
    closingPrice = 0

    latestDate = datetime.now().strftime("%Y-%m-%d")
    fromDate = datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d')

    result = getPriceInfo(stockCode, fromDate, latestDate)

    num_record = len(result)
    if num_record == 0:
        logging.info("result[] is empty")
    else:
        if numpy.isnan(result[num_record-1]):
            closingPrice = result[num_record - 2]
        else:
            closingPrice = result[num_record - 1]

    logging.info("last closing price: [{price}]".format(price=closingPrice))
    return closingPrice



def getStockInfo(stockCode, fromDate, toDate):
    listStockCodes = "T " + stockCode

    # pprint.pprint("getStockInfo: stockcode = {0} {1} {2}".format(listStockCodes, fromDate, toDate))
    logging.info("getStockInfo: stockcode = {0} {1} {2}".format(listStockCodes, fromDate, toDate))
    data = yf.download(listStockCodes, start=fromDate, end=toDate, group_by="ticker")

    # pprint.pprint("getStockInfo: data {0}".format(data))
    logging.info("getStockInfo: data {0}".format(data))

    return data[stockCode]



def getTodayStockInfo(stockCode):
    latestDate = datetime.now().strftime("%Y-%m-%d")
    fromDate = datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d')

    result = getStockInfo(stockCode, fromDate, latestDate)

    num_record = len(result)
    rtnValue = []
    if num_record == 0:
        pprint.pprint("result[] is empty")
    else:
        rtnValue = result['Close'].tolist()

    return json.dumps(rtnValue)



def getPriceInfo(stockCode, fromDate, toDate):

    values = getStockInfo(stockCode, fromDate, toDate)

    result = values['Close'].tolist()
    return result


