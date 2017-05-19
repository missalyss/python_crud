from flask import render_template, request, url_for, redirect
from app import app, models, db
from flask_sqlalchemy import SQLAlchemy

@app.route('/')
def index():
    sandwiches = models.Sandwich.query.all()
    return render_template('index.html', sandwiches=sandwiches)

@app.route('/index/')
def maybe():
    return "does this work too?"

@app.route('/new_sandwich', methods=['POST'])
def new_sandwich():
    sandwich = models.Sandwich(request.form['name'], request.form['isSandwich'])
    db.session.add(sandwich)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()
