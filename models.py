from sqlalchemy.dialects.postgresql import JSON
from hello import app, db

class Superhero(db.Model):
    __bind_key__ = 'two'
    __tablename__ = 'superhero'
    id = db.Column('superhero_id', db.Integer, primary_key = True)  
    name = db.Column(db.String(100)) 
    power = db.Column(db.String(100)) 
    level = db.Column(db.Integer) 
    def __init__(self, name, power, level):  
        self.name = name  
        self.power = power  
        self.level = level  
    def __repr__(self):
        return '<id> {}'.format(self.id)


#https://stackoverflow.com/questions/51783300/flask-migrate-no-changes-detected-to-schema-on-first-migration/59986736#59986736
