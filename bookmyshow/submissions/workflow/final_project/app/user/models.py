from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    phone = db.Column(db.Integer,unique=True)

    def __init__(self,name,username,email, password,phone):
        self.name = name
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.phone = phone

    def to_dict(self):
        return {
            'id' : self.id,
            'username' : self.username,
            'email': self.email,    
        }
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return "User<%d> %s" % (self.id, self.email)
