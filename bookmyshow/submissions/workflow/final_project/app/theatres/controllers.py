from flask import Blueprint	, request, session, jsonify, redirect, render_template	
from sqlalchemy.exc import IntegrityError
from sqlalchemy import and_
from app import db
from .models import Theatres
from app.movies.models import Movies
from app.blocked.models import Blocked
#import json

mod_theatres = Blueprint('theatres', __name__)

@mod_theatres.route('/payment',methods=['GET'])
def final():
	return render_template('final.html')

@mod_theatres.route('/add_theatre',methods=['POST'])
def add_theatres():
	try:
		Threatre_Name = request.form['Theatre_Name']
		Threatre_Type = request.form['Theatre_Type']
		Threatre_Desc = request.form['Theatre_Desc']
		Threatre_Contact = request.form['Theatre_Contact']

	except KeyError as e:
		return jsonify(success=False,message="%s not sent in the request" % e.args), 400
	theatre = Theatres(Threatre_Name,Threatre_Type,Threatre_Desc,Threatre_Contact)
	db.session.add(theatre)

	try:
		db.session.commit()
	except IntegrityError as e:
		return jsonify(success=False, message="This theatre already exists"), 400
	return redirect('/admin')


'''@mod_theatres.route('/blocked',methods=['GET'])
def q():
	return redirect('/payment')
'''

@mod_theatres.route('/Medium/<movie_name>/<theatre_name>/<time>',methods=['GET','POST'])
def med_seats(movie_name,theatre_name,time):
	if request.method=='GET':
		return render_template('medium_seats.html',theatre_name=theatre_name,time=time,movie_name=movie_name)
	elif request.method=='POST':
		try:
			movie=Movies.query.filter(Movies.Movie_Name==movie_name).first()
			theatre=Theatres.query.filter(Theatres.Theatre_Name==theatre_name).first()
			block=Blocked.query.filter(and_(Blocked.Movie_Id==movie.id,Blocked.Theatre_Id==theatre.id)).first()
			arr=request.form['arr']
		except KeyError as e:
			return jsonify(success=False,message="%s not sent in the request" % e.args), 400
		if block is None:
			seats=eval("[[],[],[],[],[]]")
		else:
			seats=eval(block.Blocked_Seats)
		print(theatre)
		arr=arr.split(',')
		print(arr)
		if time=="9AM":
			for i in arr:
				seats[0].append(i)
		elif time=="12PM":
			for i in arr:
				seats[1].append(i)
		elif time=="3PM":
			for i in arr:
				seats[2].append(i)
		elif time=="6PM":
			for i in arr:
				seats[3].append(i)
		elif time=="9PM":
			for i in arr:
				seats[4].append(i)
		print(seats)
		seats=repr(seats)
		if block is None:
			u=Blocked(movie.id,theatre.id,seats)
			db.session.add(u)
			db.session.commit()
		else :
			block.Blocked_Seats=seats
			db.session.commit()
		return redirect('/payment')		

@mod_theatres.route('/Small/<movie_name>/<theatre_name>/<time>',methods=['GET','POST'])
def small_seats(movie_name,theatre_name,time):
	if request.method=='GET':
		return render_template('small_seats.html',theatre_name=theatre_name,time=time,movie_name=movie_name)
	elif request.method=='POST':
		try:
			movie=Movies.query.filter(Movies.Movie_Name==movie_name).first()
			theatre=Theatres.query.filter(Theatres.Theatre_Name==theatre_name).first()
			block=Blocked.query.filter(and_(Blocked.Movie_Id==movie.id,Blocked.Theatre_Id==theatre.id)).first()
			arr=request.form['arr']
		except KeyError as e:
			return jsonify(success=False,message="%s not sent in the request" % e.args), 400	
		if block is None:
			seats=eval("[[],[],[],[],[]]")
		else:
			seats=eval(block.Blocked_Seats)	
		print(theatre)
		arr=arr.split(',')
		print(arr)
		if time=="9AM":
			for i in arr:
				seats[0].append(i)
		elif time=="12PM":
			for i in arr:
				seats[1].append(i)
		elif time=="3PM":
			for i in arr:
				seats[2].append(i)
		elif time=="6PM":
			for i in arr:
				seats[3].append(i)
		elif time=="9PM":
			for i in arr:
				seats[4].append(i)
		print(seats)
		seats=repr(seats)
		if block is None:
			u=Blocked(movie.id,theatre.id,seats)
			db.session.add(u)
			db.session.commit()
		else :
			block.Blocked_Seats=seats
			db.session.commit()
		return redirect('/payment')		



@mod_theatres.route('/Big/<movie_name>/<theatre_name>/<time>',methods=['GET','POST'])
def seats(movie_name,theatre_name,time):
	if request.method=='GET':
		return render_template('big_seats.html',movie_name=movie_name,theatre_name=theatre_name,time=time)
	elif request.method=='POST':
		try:
			movie=Movies.query.filter(Movies.Movie_Name==movie_name).first()
			theatre=Theatres.query.filter(Theatres.Theatre_Name==theatre_name).first()
			block=Blocked.query.filter(and_(Blocked.Movie_Id==movie.id,Blocked.Theatre_Id==theatre.id)).first()
			arr=request.form['arr']
		except KeyError as e:
			return jsonify(success=False,message="%s not sent in the request" % e.args), 400
		if block is None:
			seats=eval("[[],[],[],[],[]]")
		else:
			try:
				seats=eval(block.Blocked_Seats)
			except:
				return jsonify(success=False,message="bad request" ), 400
		print(theatre)
		arr=arr.split(',')
		print(arr)
		if time=="9AM":
			for i in arr:
				seats[0].append(i)
		elif time=="12PM":
			for i in arr:
				seats[1].append(i)
		elif time=="3PM":
			for i in arr:
				seats[2].append(i)
		elif time=="6PM":
			for i in arr:
				seats[3].append(i)
		elif time=="9PM":
			for i in arr:
				seats[4].append(i)
		print(seats)
		seats=repr(seats)
		if block is None:
			u=Blocked(movie.id,theatre.id,seats)
			db.session.add(u)
			db.session.commit()
		else :
			try:
				block.Blocked_Seats=seats
				db.session.commit()
			except:
				return jsonify(success=False,message="error"), 400
		return redirect('/payment')		

