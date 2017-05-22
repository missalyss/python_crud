from flask import render_template, request, url_for, redirect
from app import app, models, db
from flask_sqlalchemy import SQLAlchemy
from app import method_override

@app.route('/')
def index():
    sandwiches = models.Sandwich.query.all()
    return render_template('index.html', sandwiches=sandwiches)

@app.route('/edit_form/<id>')
def edit_form(id):
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    return render_template('edit_form.html', sandwich=sandwich)

@app.route('/edit/<id>')
def put(id):
    sandwich = models.Sandwich(request.form['name'], request.form['isSandwich'])
    db.session.add(sandwich)
    db.session.commit()
    return redirect('/')

@app.route('/delete/<id>', methods=['DELETE'])
def destroy(id):
    sandwich = models.Sandwich('name', 'isSandwich')
    db.session.delete(sandwich)
    db.session.commit()
    return redirect('/')

@app.route('/<id>')
def show(id):
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    return render_template('show.html', sandwich=sandwich)

@app.route('/new_sandwich', methods=['POST'])
def new_sandwich():
    sandwich = models.Sandwich(request.form['name'], request.form['isSandwich'])
    db.session.add(sandwich)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()
