from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import logging
import mktdata

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class api_root(Resource):
    def get(self):
        print('hello world!')
        return {'src': 'version 0.0.1'}

class api_healthcheck(Resource):
    def get(self):
        return {'src': 'testing'}

class api_getStockPrice(Resource):
    def get(self, stockcode):
        ticker = mktdata.getTodayPrice(stockcode)
        return ticker

api.add_resource(api_root, '/')
api.add_resource(api_healthcheck, '/test')
api.add_resource(api_getStockPrice, '/get_price/<string:stockcode>')


if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S',
                        level=logging.INFO)
    app.run(host="0.0.0.0", port=int("80"), debug=True)

