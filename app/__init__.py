from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python_crud_sandwiches'
db = SQLAlchemy(app)

from app import routes, models
