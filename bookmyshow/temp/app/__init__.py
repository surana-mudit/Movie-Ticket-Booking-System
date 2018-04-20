# Import flask and template operators
from flask import Flask, render_template, session, jsonify
from flask_cors import CORS, cross_origin
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from functools import wraps

# Define the WSGI application object
app = Flask(__name__)
cors = CORS(app)

# Configurations
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
'''@app.errorhandler(404)
def not_found(error):
   return render_template('index.html'), 200
'''
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
from app.theatres.controllers import mod_theatres
from app.movies.controllers import mod_movies
from app.profile.controllers import mod_profile
# Register blueprint(s)
app.register_blueprint(mod_user)
app.register_blueprint(mod_theatres)
app.register_blueprint(mod_movies)
app.register_blueprint(mod_profile)
# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

if __name__=="__main__":
    app.run(host='0.0.0.0')
