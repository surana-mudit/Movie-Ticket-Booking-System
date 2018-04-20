from flask import Blueprint, request, session, jsonify, render_template, redirect
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Movies

mod_movies = Blueprint('movies', __name__)



@mod_movies.route('/rate',methods=['POST'])
def rate():
	rating=request.form['rate']
	movie_name=request.form['movie_name']
	user = request.form['user']
	movie=Movies.query.filter(Movies.Movie_Name==movie_name).first()
	if not user in eval(movie.User_Rated):
		movie.User_No=movie.User_No+1
		c=movie.User_No
		db.	session.commit()
		if movie.Rating=="NR":
			movie.Rating = repr(int(rating)*25)+"%"
		else:
			q=movie.Rating
			w=q.replace("%","")
			r=int(float(w)/25.0)
			t=int(float(rating))
			r=r*(c-1)+t
			print(c,type(c))
			movie.Rating=repr(int((r*25)/c))+"%"
			db.session.commit()
		a=eval(movie.User_Rated)
		a.append(user)
		print(a)
		movie.User_Rated=repr(a)
		db.session.commit()
		return jsonify(success="Thank You For Rating")
	else:
		return jsonify(success="Rated Already")

@mod_movies.route('/add_movie',methods=['POST'])
def new_movies():
	try:
		Movie_Name = request.form['Movie_Name']
		Language = request.form['Language']
		Cast = request.form['Cast']
		Desc = request.form['Desc']
		Release_Date = request.form['Release_Date']
		Closing_Date = request.form['Closing_Date']

	except KeyError as e:
		return jsonify(success=False,message="%s not sent in the request" % e.args), 400

	movie = Movies(Movie_Name,Language,Cast,Desc,Release_Date,Closing_Date,"NR",0,"[]")
	db.session.add(movie)
	try:
		db.session.commit()
	except IntegrityError as e:
		return jsonify(success=False, message="This movie already exists"), 400

	return redirect('/admin')


@mod_movies.route('/remove_movie',methods=['POST'])
def remove_movie():
	try:
		Movie_Name = request.form['Movie_Name']
		for movie in Movies.query.filter(Movie_Name = Movie_Name).all():
			db.session.delete(movie)
		db.session.commit()

	except KeyError as e:
		return jsonify(success=False,message="%s not sent in the request" % e.args), 400
