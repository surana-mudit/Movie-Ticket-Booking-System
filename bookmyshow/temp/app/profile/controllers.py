from flask import Blueprint, request, session, jsonify,redirect , render_template
from sqlalchemy.exc import IntegrityError
from app import db
from .models import Profile
from app.user.models import User

mod_profile=Blueprint('profile', __name__)

@mod_profile.route('/profile',methods=['GET','POST'])
def show():
	if request.method == 'GET':
		user=User.query.filter(User.id==session['user_id']).first()
		profile=Profile.query.filter(Profile.User_Name==user.username).all()
		array=[]
		count=1
		for i in profile:
			j=i.to_dict()
			j['id']=count
			array.append(j)
			count=count+1
		return render_template('profile.html',username=user.username,email=user.email,arr=array)
	else:
		user=User.query.filter(User.id==session['user_id']).first()
		movie_name=request.form['movie_name']
		theatre_name=request.form['theatre_name']
		arr=request.form['arr']
		date=request.form['date']
		time=request.form['time']
		show_time=request.form['show_time']
		u=Profile(user.username,movie_name,theatre_name,time,date,arr,show_time)
		db.session.add(u)
		db.session.commit()
		return redirect('/payment')

