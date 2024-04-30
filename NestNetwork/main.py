from flask import Flask, render_template, request, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_manager, LoginManager
from flask_login import login_required, current_user
<<<<<<< HEAD
<<<<<<< HEAD

# My db connec
local_server = True
app = Flask(__name__)  # creating object of class flask
app.secret_key = 'sasa'
=======
#sssssss yoyoyoyoyoyoyoyoyo
=======
#HELLO WORLD
#sssssss yoyoyoyoyoyoyoyoyo 2134
>>>>>>> a079bf0229f32dc84f1eabc4517f496ea28556dc
#My db connec
local_server=True
app=Flask(__name__) #creating object of class flask
app.secret_key='sasa'
>>>>>>> f27651e6bc5aa6e3f87ed0ea692d3008c91427ce

# this for getting unique user access: unique page for each user:
<<<<<<< HEAD
# idetifies the app that loginManager start to set policies for it
login_manager = LoginManager(app)
# specify the name of the view function (or the endpoint) that handles user logins. When an unauthorized user attempts..
login_manager.login_view = 'Login'
# ,to access a route or a resource that requires the user to be logged in..
# ,Flask-Login automatically redirects the user to the URL associated with the view function specified in login_manager.login_view.


=======
login_manager=LoginManager(app) #idetifies the app that loginManager start to set policies for it
login_manager.login_view='login' #specify the name of the view function (or the endpoint) that handles user logins. When an unauthorized user attempts..
                                 # ,to access a route or a resource that requires the user to be logged in.. 
                                 # ,Flask-Login automatically redirects the user to the URL associated with the view function specified in login_manager.login_view.
>>>>>>> a079bf0229f32dc84f1eabc4517f496ea28556dc
@login_manager.user_loader
def load_user(stud_id):
    return Stud.query.get(int(stud_id))

@login_manager.user_loader
def load_user(prof_id):
    return Prof.query.get(int(prof_id))


# ----DB CONNECTION:
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:username:password@localhost/database_table_name//' # Connection template line for database
# URL:https://www.example.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
# set some configuration values like the URL of the database, secret key, etc...
# --RETRIEVING DATA
# username: root, password: blank, database_name: hms
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hnn'
db = SQLAlchemy(app)  # creating object(Database) of class SQLALCHEMY


# Main Tables
class Stud(UserMixin, db.Model):
    stud_id = db.Column(db.Integer, primary_key=True)  # Defining Attributes
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    uni_email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    uni = db.Column(db.String(50))
    faculty = db.Column(db.String(50))
    depart = db.Column(db.String(50))
    gender = db.Column(db.String(50))


class Prof(UserMixin, db.Model):
    prof_id = db.Column(db.Integer, primary_key=True)  # Defining Attributes
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    uni_email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    uni = db.Column(db.String(50))
    faculty = db.Column(db.String(50))
    depart = db.Column(db.String(50))
    gender = db.Column(db.String(50))

# ----PASSING endpoints od eachpage and run functions


@app.route("/")
def homepage():  # main-page
    # Loading the HTML page
    return render_template("first_page.html", pagetitle="Homepage")


@app.route("/choose")
def choose():
    return render_template("choose.html", pagetitle="Choose")


@app.route("/signup_stud", methods=['POST', 'GET'])
def signup_stud():
    # Checking IF Submit button(signup) is pressed ('action' is activated)
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        uni_email = request.form.get('uni_email')
        password = request.form.get('password')
        uni = request.form.get('uni')
        faculty = request.form.get('faculty')
        depart = request.form.get('depart')
        gender = request.form.get('gender')

        # Checks for duplicate emails
        # authinticate if the email entered already exist
        stud = Stud.query.filter_by(uni_email=uni_email).first()
        if stud:
<<<<<<< HEAD
            flash("Email Already Exist", "warning")
=======
            # flash("Email Already Exist","warning")
            print("INVALID")
>>>>>>> fa5e13f0ff48f402d1b39934b9333f8e854192d5
            return render_template("signup_stud.html")
        # enhanced password: password is hashed(encrypted) in database to maintain security
        # encpassword=generate_password_hash(password)
        # ---SENDING DATA
        new_stud = Stud(first_name=first_name,
                        last_name=last_name,
                        uni_email=uni_email,
                        password=password,
                        uni=uni,
                        faculty=faculty,
                        depart=depart,
                        gender=gender)
        db.session.add(new_stud)
        db.session.commit()
        return render_template("login.html")  # NOT EXECUTEDDDD
    return render_template("signup_stud.html", pagetitle="Student")


@app.route("/signup_prof", methods=['POST', 'GET'])
def signup_prof():

    # Checking IF Submit button(signup) is pressed ('action' is activated)
    if request.method == "POST":
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        uni_email = request.form.get('uni_email')
        password = request.form.get('password')
        uni = request.form.get('uni')
        faculty = request.form.get('faculty')
        depart = request.form.get('depart')
        gender = request.form.get('gender')

    # Checks for duplicate emails
        # authinticate if the email entered already exist
        prof = Prof.query.filter_by(uni_email=uni_email).first()
        if prof:
            flash("Email Already Exist", "warning")
            return render_template("signup_prof.html")
            # enhanced password: password is hashed(encrypted) in database to maintain security
            # encpassword=generate_password_hash(password)
            # ---SENDING DATA
        new_prof = Prof(first_name=first_name,
                        last_name=last_name,
                        uni_email=uni_email,
                        password=password,
                        uni=uni,
                        faculty=faculty,
                        depart=depart,
                        gender=gender)
        db.session.add(new_prof)
        db.session.commit()
        return render_template("login.html")  # NOT EXECUTEDDDD
    return render_template("signup_prof.html", pagetitle="Proof")


@app.route("/login", method=['POST','GET'])
def login():
<<<<<<< HEAD
    return render_template("login.html", pagetitle="Login")
=======
        if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
            uni_email=request.form.get('uni_email')
            password=request.form.get('password') 
            email_found=Stud.query.filter_by(uni_email=uni_email).first()
            email_found=Prof.query.filter_by(uni_email=uni_email).first()
            # pass_true=check_password_hash(email_found.password,password)
            
            if email_found and email_found.password==password:
                print("VALID")
                login_user(email_found)
                return redirect(url_for('first_page'))
                # return render_template("bookings.html")
            else:
                flash("Invalid Credendtials")
                print("INVALID CREDINTIALS")
                return render_template('login.html')    

        return render_template("login.html", pagetitle="Login")
>>>>>>> fa5e13f0ff48f402d1b39934b9333f8e854192d5


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication
    app.run(debug=True, port=5000)
