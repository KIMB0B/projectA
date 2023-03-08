from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from src import STT
from src import GPT
from src import NaverShopping
import config

DB_USER = config.db_user
DB_PASSWORD = config.db_password
DB_HOST = config.db_host
DB_DATABASE = config.db_database

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_DATABASE}"
db = SQLAlchemy(app)

class Requests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    request = db.Column(db.String(80), unique=False, nullable=True)
    keyword = db.Column(db.String(120), unique=False, nullable=True)

    def __repr__(self):
        return '<Requests %r>' % self.name

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
    keyword = GPT.getResponse(req+"라는 말에서 가장 중요한 명사 키워드 하나만 골라줘")

    requestModel = Requests(request=req, keyword=keyword)
    db.session.add(requestModel)
    db.session.commit()
    # query all users
    requests = Requests.query.all()
    for r in requests:
        print(r.request, r.keyword)

    return keyword


@app.route('/getProducts', methods=['GET'])
def getProducts():
    product = request.args.to_dict()['product']
    return NaverShopping.getProductsInNaverShopping(product)


if __name__ == '__main__':
    app.run()
