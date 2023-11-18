from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

App = Flask(__name__)

App.secret_key='ádfghjkrertyuioiuytfdfghjkjytrertyujhgfd'

App.config["SQLALCHEMY_DATABASE_URI"] ='mysql+pymysql://root:%s@localhost/saleapp?charset=utf8mb4' % quote('Tandat25102003')
App.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
db = SQLAlchemy(app=App)
login= LoginManager(app=App)