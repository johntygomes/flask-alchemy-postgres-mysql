from flask import Flask, flash, url_for, redirect, render_template
from markupsafe import escape
from flask_sqlalchemy import SQLAlchemy
import os
################################################################
app = Flask(__name__)
control=1

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////G/Flask/project1/one.db'
app.config['SQLALCHEMY_BINDS'] = {
                 'two': 'postgresql://postgres:1234@localhost:5432/myheroes',
                 'three': 'mysql://root:''@localhost/mycompanies'
                    }
###########
db = SQLAlchemy(app)
################################################################
from models import Superhero
from models2 import Company
db.create_all(bind='two')
db.create_all(bind='three')

################################################################
sup1=Superhero('Spiderman','Webs',87)
sup2=Superhero('Hulk','Green Muscles',92)
sup3=Superhero('Iron Man','Insane Tech',98)
sup4=Superhero('Thor','Hammer',95)
db.session.add(sup1)
db.session.add(sup2)
db.session.add(sup3)
db.session.add(sup4)

com1=Company('Facebook','Mark ZuckerBerg',2004,85965)
com2=Company('Google','Larry Page',1998,146000)
com3=Company('Facebook','Jeff Bezos',1994,386000)
com4=Company('Tesla','Elon Musk',2003,31536)
db.session.add(com1)
db.session.add(com2)
db.session.add(com3)
db.session.add(com4)

db.session.commit()
#############################
@app.route('/')
def hello_world():
    return render_template('hello_world.html')

@app.route('/postgresql')
def the_postgresql_page():
    return render_template('postgresql.html',superheroes=Superhero.query.all())
    #sup=Superhero("Spiderman","Webs",87)
    #db.session.add(sup)
    #db.commit()

@app.route('/mysql')
def the_mysql_page():
    return render_template('mysql.html',companies=Company.query.all())

with app.test_request_context():
    print(url_for('hello_world'))
    print(url_for('the_postgresql_page'))
    print(url_for('the_mysql_page'))





##DOCUMENTATIONS
#1 https://flask.palletsprojects.com/en/1.1.x/quickstart/
#2 https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
#3 https://www.javatpoint.com/flask-sqlalchemy