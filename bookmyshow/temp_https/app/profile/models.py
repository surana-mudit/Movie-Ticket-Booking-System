from flask_sqlalchemy import SQLAlchemy
from app import db

class Profile(db.Model):
	__tablename__ = 'profile'
	id = db.Column(db.Integer , primary_key=True,autoincrement=True)
	User_Name = db.Column(db.String(120))
	Movie_Name = db.Column(db.String(120))
	Theatre_Name = db.Column(db.String(120))
	Time = db.Column(db.String(500))
	Date = db.Column(db.String(100))
	Seats = db.Column(db.String(1000))
	Show_Time = db.Column(db.String(500))

	def __init__(self,User_Name,Movie_Name,Theatre_Name,Time,Date,Seats,Show_Time	):
		self.User_Name = User_Name
		self.Movie_Name = Movie_Name
		self.Theatre_Name = Theatre_Name
		self.Time = Time
		self.Date = Date
		self.Seats = Seats
		self.Show_Time = Show_Time

	def to_dict(self):
		return {
			'User_Name' : self.User_Name,
			'Movie_Name' : self.Movie_Name,
			'Theatre_Name' : self.Theatre_Name,
			'Time' : self.Time,
			'Date' : self.Date,
			'Seats' : self.Seats,
			'Show_Time' : self.Show_Time,
		}
