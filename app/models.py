from app import db

class Sandwich(db.Model):
    __tablename__ = "sandwiches"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    isSandwich = db.Column(db.Boolean())

    def __init__(self, name, isSandwich):
        self.name = name
        self.isSandwich = isSandwich

    def __repr__(self):
        sandwich = '"id":"{}", "name": "{}", "isSandwich": "{}"'.format(self.id, self.name, self.isSandwich)
        return sandwich
