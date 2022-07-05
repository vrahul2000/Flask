from flask_wtf import FlaskForm
from sqlalchemy import Float
from wtforms import PasswordField, StringField, SubmitField, validators , IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegisterForm(FlaskForm):
  EmpName = StringField("EmpName",validators=[DataRequired(),Length(min=3,max=100)])
  EmpSalary = FloatField("EmpSalary",validators=[DataRequired('Float Value Required')])
  EmpId= StringField("EmpId",validators=[DataRequired(),Length(min=3,max=100000)])
  TechArea= StringField("TechArea",validators=[DataRequired(),Length(min=3,max=100)])
  password= PasswordField("Password",validators=[DataRequired(),Length(min=5,max=8)])
  confirm_password= PasswordField("Confirm_Password",validators=[DataRequired(),EqualTo('password')])
  submit = SubmitField("Register")
  
class LoginForm(FlaskForm):
  EmpId= StringField("EmpId",validators=[DataRequired(),Length(min=3,max=100000)])
  password= PasswordField("Password",validators=[DataRequired(),Length(min=5,max=8)])
  submit = SubmitField("Login") 