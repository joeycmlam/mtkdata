import pprint
import mktdata
import logging


if __name__ == '__main__':

    stockCode = 'C-PN'

    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=logging.INFO)

    logging.info("stock {0} ".format(stockCode))

    price = mktdata.getTodayPrice(stockCode)

    logging.info("price {0} = {1}".format(stockCode, price))


