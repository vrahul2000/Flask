from flask import Flask, redirect,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from .config import BaseConfig
from flask_migrate import Migrate

app= Flask(__name__)    

db= SQLAlchemy(app) 
migrate= Migrate(app,db)
app.config.from_object(BaseConfig)


from myapp import routes,models,form

app.run(debug=True)