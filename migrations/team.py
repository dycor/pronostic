from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql7248339:XX1etS2T8C@sql7.freemysqlhosting.net:3306/sql7248339'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Team(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   image = db.Column(db.String(255))

def __init__(self, name, image):
   self.name = name
   self.image = image