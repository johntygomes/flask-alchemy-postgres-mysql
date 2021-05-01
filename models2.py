from sqlalchemy.dialects.postgresql import JSON
from hello import app, db

class Company(db.Model):
    __bind_key__ = 'three'
    __tablename__ = 'company'
    id = db.Column('company_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    owner = db.Column(db.String(100))
    year = db.Column(db.Integer)
    revenue = db.Column(db.Integer)
    def __init__(self, name, owner, year, revenue):
        self.name = name
        self.owner = owner
        self.year = year
        self.revenue = revenue
    def __repr__(self):
        return '<id> {}'.format(self.id)