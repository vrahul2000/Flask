from flask import flash, redirect, render_template, url_for
from myapp import app
#from form import RegisterForm,LoginForm
#from .models import Quotes
from .form import RegisterForm,LoginForm
#from helloapp import app, db
from sqlalchemy import ForeignKey, null
from myapp import db,models
from flask import flash



@app.route('/')
def home():
    return render_template('home_feedback.html')

@app.route('/register',methods=['GET', 'POST'])
def reg():
    form = RegisterForm()
    db.create_all()
    render_template("register.html",form=form)
    if form.validate_on_submit():
        found_user=models.Company.query.filter_by(EmpId=form.EmpId.data).first()
        if found_user:
            if  str(found_user.EmpId)==form.EmpId.data:
                return render_template("feedback2.html")
        else:
            db.session.add(models.Company(EmpName=form.EmpName.data,EmpSalary=form.EmpSalary.data,EmpId= form.EmpId.data,password=form.password.data))
            db.session.add(models.EmpTechArea(EmpName=form.EmpName.data,TechArea=form.TechArea.data,EmpId= form.EmpId.data))
            db.session.commit()
            return render_template("reg_feedback.html")
    else:
        return render_template("register.html",form=form)
@app.route('/login',methods=['GET', 'POST'])
def log():
    form= LoginForm()
    render_template("login.html",form=form)
    found_user=models.Company.query.filter_by(EmpId=form.EmpId.data).first()
    found_user2=models.EmpTechArea.query.filter_by(EmpId=form.EmpId.data).first()

    #found_user=models.Company.query.all()

    if form.validate_on_submit():
        if found_user:
            if found_user.password==form.password.data and str(found_user.EmpId)==form.EmpId.data:
                return render_template("view.html",a=found_user,b=found_user2)
            else:
                flash("Incorrect UserId/Password")
                return redirect(url_for("log"))
        else:
            return render_template("feedback.html")
    else:
        if found_user==null:
            return redirect(url_for("reg"))
        return render_template("login.html",form=form)


@app.route('/admin')
def admin():
    a=models.Company.query.all()
    b=models.EmpTechArea.query.all()
    return render_template("admin.html",a=a,b=b,l=len(a))


    