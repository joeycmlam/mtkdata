from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
import mktdata

app = Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
api = Api(app)

class api_root(Resource):
    def get(self):
        print('hello world!')
        return {'mktdata': 'version 0.0.1'}

class api_getStockPrice(Resource):
    def get(self, stockcode):
        price = mktdata.getTodayPrice(stockcode)
        return {'price': price}

api.add_resource(api_root, '/')
api.add_resource(api_getStockPrice, '/get_price/<string:stockcode>')


if __name__ == '__main__':
    app.run()

