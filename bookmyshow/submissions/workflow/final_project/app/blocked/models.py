from flask_sqlalchemy import SQLAlchemy
from app import db

class Blocked(db.Model):
	__tablename__ = 'blocked'
	id= db.Column(db.Integer,primary_key=True,autoincrement=True)
	Movie_Id = db.Column(db.Integer)
	Theatre_Id = db.Column(db.Integer)
	Blocked_Seats = db.Column(db.String(5000))

	def __init__(self,Movie_Id,Theatre_Id,Blocked_Seats):
		self.Movie_Id=Movie_Id
		self.Theatre_Id=Theatre_Id
		self.Blocked_Seats=Blocked_Seats

	def to_dict(self):
		return {
			'Movie_Id': self.Movie_Id,
			'Theatre_Id': self.Theatre_Id,
			'Blocked_Seats': self.Blocked_Seats
		}
		
	def __repr__(self):
		return "Theatre_Id %s , Movie_Id %s"%(self.Theatre_Id,self.Movie_Id)