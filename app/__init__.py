from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python_crud_sandwiches'
heroku = Heroku(app)
db = SQLAlchemy(app)

from app import routes, models
