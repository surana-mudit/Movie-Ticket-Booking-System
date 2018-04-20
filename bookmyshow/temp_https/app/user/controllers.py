from flask import Blueprint, request, session, jsonify,redirect , render_template
from sqlalchemy.exc import IntegrityError
from app import db
from .models import User
from app.movies.models import Movies
from app.theatres.models import Theatres
from werkzeug.security import generate_password_hash, check_password_hash


mod_user=Blueprint('user', __name__)


@mod_user.route('/register',methods=['POST', 'GET'])
def addUser():
    if request.method == 'POST':
        try:
            name = request.form['name']
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            retype_password = request.form['retype_password']
            phone = request.form['phone']
        except KeyError as e:
            return jsonify(success=False, message="%s not sent in the request" % e.args), 400

        if '@' not in email:
            return jsonify(success=False, message="Please enter a valid email"), 400
        if password!=retype_password:
    	    return jsonify(success=False, message="Passwords Do Not Match"),400
        if '@' in username:
            return jsonify(success=False, message="username must be alpha-numeric"),400    
        u = User(name,username,email, password,phone)
        db.session.add(u)
        try:
            db.session.commit()
        except IntegrityError as e:
            return jsonify(success=False, message="This email/username already exists"), 400
        return redirect('https://localhost:5000/login')
    elif request.method == 'GET':
        return render_template('signup.html')

@mod_user.route('/login',methods=['GET'])
def view1():
    return render_template('login.html')

@mod_user.route('/login', methods=['GET'])
def check_login():
    if 'user_id' in session:
        user = User.query.filter(User.id == session['user_id']).first()
        return jsonify(success=True, user=user.to_dict())

    return jsonify(success=False), 401

@mod_user.route('/login', methods=['POST'])
def login():
    try:
        email_username = request.form['email_username']
        password = request.form['password']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    if email_username == 'admin@admin.com' or email_username=='admin':
    	if password == 'admin':
            session['user_id']=1
            print(session['user_id'])
            return redirect('/admin')
    else: 
        user = User.query.filter(User.email == email_username).first()
        if user is None:
            user = User.query.filter(User.username == email_username).first()
        if user is None or not user.check_password(password):
            return jsonify(success=False, message="Invalid Credentials"), 400

        session['user_id'] = user.id
        print(session['user_id'])
        return redirect('https://localhost:5000/movies')


@mod_user.route('/logout', methods=['GET'])
def logout():
    print(session['user_id'])
    session.pop('user_id')
    return redirect('https://localhost:5000/login')

@mod_user.route('/movies',methods=['GET'])
def show():
    return render_template('movies.html')

@mod_user.route('/movies',methods=['POST'])
def show1():
    x={}
    x["movies"]=[]
    for i in Movies.query.all():
        x["movies"].append(i.to_dict())

    print(x)
    if 'user_id' in session:
        user1=User.query.filter(User.id==session['user_id']).first()
        print(user1.to_dict()['username'])
        return jsonify(state="LOGOUT",url="/logout",movies=x,user=user1.to_dict()['username'])
    else:
        return jsonify(state="SIGN IN",url="/login",movies=x)

@mod_user.route('/',methods=['GET'])
def add():
    db.session.add(User("admin","admin","admin@admin.com","admin",9898908717))
    db.session.commit()
    db.session.add(Movies("Begumjaan","Hindi","Vidya Balan","Nice Movie","2017-04-04","2017-04-11","NR",0,"[]"))
    db.session.commit()
    db.session.add(Movies("Badrinath","Hindi","alia bhatt","Nice Movie","2017-04-04","2017-04-11","NR",0,"[]"))
    db.session.commit()
    return redirect('/home')

@mod_user.route('/home',methods=['GET'])
def view():
	return render_template('index.html')

@mod_user.route('/admin',methods=['GET'])
def view3():
	return render_template('admin.html')

@mod_user.route('/movies/show/<name>',methods=['GET'])
def view4(name):
	return render_template('show.html',name=name)

@mod_user.route('/movies/show/<name>',methods=['POST'])
def view5(name):
	movie=Movies.query.filter(Movies.Movie_Name== name).first()
	return jsonify(movie=movie.to_dict())



@mod_user.route('/theatres',methods=['POST'])
def show2():
    x={}
    x["theatres"]=[]
    name=request.form['name']
    for i in Theatres.query.filter(Theatres.Movie_Name==name).all():
        x["theatres"].append(i.to_dict())
        
    print(x)
    if 'user_id' in session:
        return jsonify(state="LOGOUT",url="/logout",theatres=x)
    else:
        return jsonify(state="SIGN IN",url="/login",theatres=x)
