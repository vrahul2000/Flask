import os

basedir=os.path.abspath(os.path.dirname('myapp'))

class BaseConfig(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir,'myapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=  os.environ.get('SECRET_KEY') or 'jkgkvkvvvvvvv'
    
    

    
        
    