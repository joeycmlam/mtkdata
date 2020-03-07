import yfinance as yf
import pprint
from datetime import date

def getDownload(stockCode):
    startDate = '2020-03-06'
    endDate = '2020-03-06'
    data = yf.download(stockCode, start=startDate, end=endDate)
    pprint.pprint(data['Close'][stockCode])



if __name__ == '__main__':

    stockCode = "SDIV TBB C-PN"
    today = date.today()
    latestDate = today.strftime("%Y-%m-%d")

    data = yf.download(stockCode, start=latestDate, end=latestDate, group_by="ticker")

    values = data['C-PN']['Close']


    pprint.pprint(values)

    price_list = value['Close'].tolist()

    pprint.pprint(price_list)


