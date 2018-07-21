from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    firstname = db.Column(db.String(30))
    lastname = db.Column(db.String(30))
    password = db.Column(db.String(50))
    rank = db.Column(db.Integer)
    birthdate = db.Column(db.Date)
    admin = db.Column(db.Boolean)

    def verify_password(self, pwd):
        return self.password == pwd