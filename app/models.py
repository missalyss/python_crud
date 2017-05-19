from app import db

class Sandwich(db.Model):
    __tablename__ = "sandiwches"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<name %r>' % self.name
