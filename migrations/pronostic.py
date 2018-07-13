from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Pronostic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_team_score = db.Column(db.Integer(2), nullable=False)
    second_team _score = db.Column(db.Integer(2), nullable=False)
    user_id = db.Column(db.Integer(120), db.ForeignKey('team.id'),nullable=False)
    match_id = db.Column(db.Integer(120), db.ForeignKey('team.id'),nullable=False)
    points = db.Column(db.Integer(120),nullable=False)
    second_team_id = db.Column(db.Integer(120), db.ForeignKey('team.id'),nullable=False)

# def __init__(self, day, hour,first_team_id,second_team_id,first_team_score,second_team_score):
#    self.day = day
#    self.hour = hour
#    self.first_team_id = first_team_id
#    self.second_team_id = second_team_id
#    self.first_team_score = first_team_score
#    self.second_team_score = second_team_score