from flask import Blueprint	, request, session, jsonify, redirect, render_template	
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_
from app import db
from .models import Blocked
from app.movies.models import Movies
from app.theatres.models import Theatres

mod_blocked=Blueprint('blocked',__name__)

@mod_blocked.route('/blocked',methods=['POST'])
def blocked_seats():
	movie_name=request.form['name']
	theatre_name=request.form['theatre_name']
	movie_id1=Movies.query.filter(Movies.Movie_Name==movie_name).first()
	movie_id=movie_id1.id
	theatre_id1=Theatres.query.filter(Theatres.Theatre_Name==theatre_name).first()
	theatre_id=theatre_id1.id
	blocked=Blocked.query.filter(and_(Blocked.Movie_Id==movie_id,Blocked.Theatre_Id==theatre_id)).first()
	if blocked is None:
		seats=[[],[],[],[],[]]
	else:
		seats=eval(blocked.Blocked_Seats)
	return jsonify(seats=seats)

