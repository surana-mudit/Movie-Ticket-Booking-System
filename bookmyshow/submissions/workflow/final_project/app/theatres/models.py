from flask_sqlalchemy import SQLAlchemy
from app import db
	
class Theatres(db.Model):
	__tablename__ = 'theatres'
	id = db.Column(db.Integer , primary_key=True,autoincrement=True)
	Theatre_Name = db.Column(db.String(120))
	Theatre_Type = db.Column(db.String(120))
	Theatre_Desc = db.Column(db.String(500))
	Theatre_Contact = db.Column(db.String(60))

	def __init__(self,Theatre_Name,Theatre_Type,Theatre_Desc,Theatre_Contact):
		self.Theatre_Name = Theatre_Name
		self.Theatre_Type = Theatre_Type
		self.Theatre_Desc = Theatre_Desc
		self.Theatre_Contact = Theatre_Contact

	def to_dict(self):
		return {
			'Theatre_Name' : self.Theatre_Name,
			'Theatre_Type' : self.Theatre_Type,
			'Theatre_Desc' : self.Theatre_Desc,
			'Theatre_Contact' : self.Theatre_Contact,
		}

	def __repr__(self):
		return "Theatre_Id %s , Theatre_Name %s , Theatre_Type %s , Theatre_Desc %s , Theatre_Contact %s" % (self.id , self.Theatre_Name , self.Theatre_Type , self.Theatre_Desc , self.Theatre_Contact)
		
