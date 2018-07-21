from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    image = db.Column(db.String(255))