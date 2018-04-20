from flask_sqlalchemy import SQLAlchemy
from app import db
	
class Theatres(db.Model):
	__tablename__ = 'theatres'
	id = db.Column(db.Integer , primary_key=True,autoincrement=True)
	Movie_Name=db.Column(db.String(120))
	Theatre_Name = db.Column(db.String(120))
	Theatre_Type = db.Column(db.String(120))
	Theatre_Desc = db.Column(db.String(500))
	Theatre_Contact = db.Column(db.String(60))
	Theatre_Seats= db.Column(db.String(10000))

	def __init__(self,Movie_Name,Theatre_Name,Theatre_Type,Theatre_Desc,Theatre_Contact,Theatre_Seats):
		self.Movie_Name = Movie_Name
		self.Theatre_Name = Theatre_Name
		self.Theatre_Type = Theatre_Type
		self.Theatre_Desc = Theatre_Desc
		self.Theatre_Contact = Theatre_Contact
		self.Theatre_Seats=Theatre_Seats

	def to_dict(self):
		return {
			'Movie_Name' : self.Movie_Name,
			'Theatre_Name' : self.Theatre_Name,
			'Theatre_Type' : self.Theatre_Type,
			'Theatre_Desc' : self.Theatre_Desc,
			'Theatre_Contact' : self.Theatre_Contact,
			'Theatre_Seats': self.Theatre_Seats
		}

	def __repr__(self):
		return "Theatre_Id %s , Theatre_Name %s , Theatre_Type %s , Theatre_Desc %s , Theatre_Contact %s" % (self.id , self.Theatre_Name , self.Theatre_Type , self.Theatre_Desc , self.Theatre_Contact)
		
