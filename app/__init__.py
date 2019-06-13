from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key =  os.urandom(50)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@192.168.1.188:1050/wsm?charset=utf8"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)

from app import view

app.debug = True
