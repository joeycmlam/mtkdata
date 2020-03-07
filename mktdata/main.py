import pprint
import importlib, importlib.util
import mktdata




def module_from_file(module_name: object, file_path: object) -> object:
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


if __name__ == '__main__':

    stockCode = 'C-PN'

    price = mktdata.getTodayPrice(stockCode)

    pprint.pprint("price {0} = {1}".format(stockCode, price))

    #clear object
    #del objMk

