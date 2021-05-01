import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = '5f352379324c22463451387a0aec5d2f'
    #SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost:5432/myheroes'
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')



class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

##Useful DOCUMENTATIONS
#1 https://flask.palletsprojects.com/en/1.1.x/quickstart/
#2 https://realpython.com/flask-by-example-part-2-postgres-sqlalchemy-and-alembic/
#3 https://www.javatpoint.com/flask-sqlalchemy
#4 https://stackoverflow.com/questions/51783300/flask-migrate-no-changes-detected-to-schema-on-first-migration/59986736#59986736
#5 https://codeloop.org/flask-tutorial-flask-sqlalchemy-with-mysql/
#6 https://flask-appbuilder.readthedocs.io/en/latest/multipledbs.html#:~:text=Because%20you%20can%20use%20Flask,class)%20multiple%20databases%20is%20supported.&text=The%20SQLALCHEMY_DATABASE_URI%20is%20the%20default,SQLALCHEMY_BINDS%20are%20the%20extra%20binds.


#set FLASK_APP=hello.py
#set APP_SETTINGS=config.DevelopmentConfig
#set DATABASE_URL="postgresql:///myheroes"
#db.create_all(bind='two')

####################IMPORTANT URL PATTERNS
#1. POSTGRESQL::   postgresql://user:password@localhost:5432/database_name
#1. POSTGRESQL::   postgresql://postgres:1234@localhost:5432/myheroes
#1. MYSQL::        mysql://user:pass@localhost:3306/database_name
#REFERENCE:: https://stackoverflow.com/questions/23839656/sqlalchemy-no-password-supplied-error