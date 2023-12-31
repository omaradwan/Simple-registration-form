from flask import Blueprint,render_template,request,redirect,flash,url_for
from.models import User,Note
from werkzeug.security import generate_password_hash, check_password_hash
from website import db
from flask_login import login_user, login_required,logout_user,current_user
auth=Blueprint('auth',__name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user =User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.hello'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html",user=current_user)        

   
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up' ,methods=['GET','POST'])
def sign():
    if request.method=='POST':
        email=request.form.get('email')
        firstName=request.form.get('firstName')
        password1=request.form.get('password1')
        password2=request.form.get('password2')
        user =User.query.filter_by(email=email).first()
        if user:
            flash('This email is already exist',category="error")
        if len(email)<4:
            flash('Email lengths must be greater than 3',category="error")#category to know what color am gonna send in red or green or whatever
        elif len(firstName)<2:
            flash('name lengths must be greater than 1',category="error")
        elif len(password1)<3:
            flash("password lengths must be greater than 2",category="error")    
        elif password1!=password2:
            flash('password does not match',category="error")    
        else:
             new_user = User(email=email, firstName=firstName, password=generate_password_hash(
                password1, method='sha256'))
             db.session.add(new_user)
             db.session.commit() 
             flash("Account created succefully!",category="success") 
             login_user(new_user, remember=True)   
             return redirect(url_for('views.hello'))
    return render_template("signup.html",user=current_user)