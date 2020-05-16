from flask import render_template, url_for, flash, redirect
from src.forms import RegistrationForm, LoginForm
from src.models import User
from src import app


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Flask | Home")

@app.route("/about")
def about():
    return render_template("about.html", title="Flask | About")
    
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Flask | REGISTER", form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == 'admin' and form.password.data == 'password':
            flash("User {0} is able to Successfully Login.".format(form.username.data), "success")
            return redirect(url_for('home'))
        else:
            flash("Login Unsuccessfull, Please check Username or Password", "danger")
    return render_template("login.html", title="Flask | LOGIN", form = form)

