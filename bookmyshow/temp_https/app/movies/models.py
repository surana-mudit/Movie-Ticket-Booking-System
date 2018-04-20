from flask_sqlalchemy import SQLAlchemy
from app import db

class Movies(db.Model):
	__tablename__ = 'movies'
	id = db.Column(db.Integer , primary_key=True,autoincrement=True)
	Movie_Name = db.Column(db.String(120),unique=True)
	Language = db.Column(db.String(120))
	Cast = db.Column(db.String(120))
	Desc = db.Column(db.String(500))
	Release_Date = db.Column(db.String(100))
	Closing_Date = db.Column(db.String(100))
	Rating =  db.Column(db.String(20))
	User_No = db.Column(db.Integer)
	User_Rated = db.Column(db.String(500))

	def __init__(self,Movie_Name,Language,Cast,Desc,Release_Date,Closing_Date,Rating,User_No,User_Rated):
		self.Movie_Name = Movie_Name
		self.Language = Language
		self.Cast = Cast
		self.Desc = Desc
		self.Release_Date = Release_Date
		self.Closing_Date = Closing_Date
		self.Rating = Rating
		self.User_No=User_No
		self.User_Rated = User_Rated

	def to_dict(self):
		return {
			'Movie_Name' : self.Movie_Name,
			'Language' : self.Language,
			'Cast' : self.Cast,
			'Desc' : self.Desc,
			'Release_Date' : self.Release_Date,
			'Closing_Date' : self.Closing_Date,
			'Rating' : self.Rating,
			'User_No' : self.User_No,
			'User_Rated' : self.User_Rated,
		}

	'''def __repr__(self):
		return "Movie_Name %s Language %s Cast %s Desc %s Release_Date %s Closing_Date %s Rating %s" % (self.Movie_Id,self.Movie_Name,self.Language,self.Cast,self.Desc,self.Release_Date,self.Closing_Date,self.Rtaing)
'''
