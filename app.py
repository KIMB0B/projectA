from flask import Flask, render_template, request
from src import STT
from src import GPT
from src import NaverShopping

app = Flask(__name__)


@app.route('/')
def goIndex():  # put application's code here
    return render_template("index.html")


@app.route('/getRequest', methods=['GET'])
def getRequest():
    req = STT.getRequest()
    return req


@app.route('/getResponse', methods=['GET'])
def getResponse():
    req = request.args.to_dict()['req']
    return GPT.getResponse(req)


@app.route('/getProducts', methods=['GET'])
def getProducts():
    product = request.args.to_dict()['product']
    return NaverShopping.getProductsInNaverShopping(product)


if __name__ == '__main__':
    app.run()
