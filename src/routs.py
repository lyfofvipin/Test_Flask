from flask import render_template, url_for, flash, redirect, request
from src.forms import RegistrationForm, LoginForm
from src.models import User
from src import app, db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Flask | Home")

@app.route("/about")
def about():
    return render_template("about.html", title="Flask | About")
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! you are now able to login.', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Flask | REGISTER", form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')[1:] if request.args.get('next') else 'home'
            return redirect(url_for(next_page))
        else:
            flash("Login Unsuccessfull, Please check Username or Password", "danger")
    return render_template("login.html", title="Flask | LOGIN", form = form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/account")
@login_required
def account():
    return render_template("account.html", title="Flask | ACCOUNT")
