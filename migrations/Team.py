from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Team(db.Model):
   id = db.Column(db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   image = db.Column(db.String(255))

def __init__(self, name, image):
   self.name = name
   self.image = image