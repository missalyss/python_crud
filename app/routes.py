from flask import render_template, request
from app import app, models

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def maybe():
    return "does this work too?"

@app.route('/new-sandwich', methods=['POST'])
def prereg():
    name = None
    if request.method == 'POST':
        name = request.form['name']
        # Check that name does not already exist (not a great query, but works)
        if not db.session.query(Sandwich).filter(Sandwich.name == name).count():
            reg = Sandwich(name)
            db.session.add(reg)
            db.session.commit()
            return render_template('post.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.run()
