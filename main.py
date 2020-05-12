from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '3092e766d8a79953890a1c765ab6ca01'

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
        flash("You has been successfully logged in.", "success")
        return redirect(url_for('home'))
    else:
        flash("Login Unsuccessfull, Please check Username or Password", "danger")
    return render_template("register.html", title="Flask | REGISTER", form = form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("User {0} is able to Successfully Login.".format(form.username.data), "success")
        return redirect(url_for('home'))
    return render_template("login.html", title="Flask | REGISTER", form = form)

if __name__ == "__main__":
    app.run(debug=True)
