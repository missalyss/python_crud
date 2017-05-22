from flask import render_template, request, url_for, redirect
from app import app, models, db
from flask_sqlalchemy import SQLAlchemy

# Index
@app.route('/')
def index():
    sandwiches = models.Sandwich.query.all()
    return render_template('index.html', sandwiches=sandwiches)

# Render edit form
@app.route('/edit_form/<id>')
def edit_form(id):
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    return render_template('edit_form.html', sandwich=sandwich)

# Update
@app.route('/edit/<id>', methods=['POST'])
def put(id):
    form = models.Sandwich(request.form['name'], request.form['isSandwich'])
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    sandwich.name = form.name
    # sandwich.isSandwich = form.isSandwich
    db.session.add(sandwich)
    db.session.commit()
    return redirect('/')

# Destroy
@app.route('/delete/<id>', methods=['POST'])
def destroy(id):
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    print(sandwich)
    if sandwich is not None:
        db.session.delete(sandwich)
        db.session.commit()
        return redirect('/')

# Show
@app.route('/<id>')
def show(id):
    sandwich = models.Sandwich.query.filter_by(id=id).first()
    return render_template('show.html', sandwich=sandwich)

# Create
@app.route('/new_sandwich', methods=['POST'])
def new_sandwich():
    sandwich = models.Sandwich(request.form['name'], request.form['isSandwich'])
    db.session.add(sandwich)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run()
