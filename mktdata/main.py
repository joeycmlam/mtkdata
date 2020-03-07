import pprint
import mktdata

if __name__ == '__main__':


    stockCode = 'C-PN'
    price = mktdata.getTodayPrice(stockCode)
    pprint.pprint("price {0} = {1}".format(stockCode, price))

