from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql7248339:XX1etS2T8C@sql7.freemysqlhosting.net:3306/sql7248339'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.String(120), nullable=False)
    hour = db.Column(db.String(120), nullable=False)
    first_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'),nullable=False)
    second_team_id = db.Column(db.Integer(), db.ForeignKey('team.id'),nullable=False)
    first_team_score = db.Column(db.Integer(), nullable=True)
    second_team_score = db.Column(db.Integer(), nullable=True)

def __init__(self, day, hour,first_team_id,second_team_id,first_team_score,second_team_score):
   self.day = day
   self.hour = hour
   self.first_team_id = first_team_id
   self.second_team_id = second_team_id
   self.first_team_score = first_team_score
   self.second_team_score = second_team_score