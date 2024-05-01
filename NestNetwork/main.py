from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin  
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import  login_user, logout_user,login_manager, LoginManager 
from flask_login import login_required, current_user
import random

#HELLO WORLD
#sssssss yoyoyoyoyoyoyoyoyo 2134
#My db connec

local_server=True
app=Flask(__name__) #creating object of class flask
app.secret_key='sasa'

# this for getting unique user access: unique page for each user:
login_manager=LoginManager(app) #idetifies the app that loginManager start to set policies for it
login_manager.login_view='login' #specify the name of the view function (or the endpoint) that handles user logins. When an unauthorized user attempts..
                                 # ,to access a route or a resource that requires the user to be logged in.. 
                                 # ,Flask-Login automatically redirects the user to the URL associated with the view function specified in login_manager.login_view.
@login_manager.user_loader
def load_user(user_id):
    user=Stud.query.get(int(user_id))
    if user is None:
        user=Prof.query.get(int(user_id))
    return user

#----DB CONNECTION:
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:username:password@localhost/database_table_name//' # Connection template line for database
#URL:https://www.example.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
#set some configuration values like the URL of the database, secret key, etc...
#--RETRIEVING DATA
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hnn' # username: root, password: blank, database_name: hms
db=SQLAlchemy(app) #creating object(Database) of class SQLALCHEMY

#######
#functions block
#1 UC, 1 LC, 1 no, symbol
# min len = 8 max = 20
def strong_pass(password):
    return len(password) >=8 and len(password) <=20 and any(char.isupper() for char in password) and not password.isalnum() and any(char.islower() for char in password) and any(char.isdigit() for char in password)

def rand_id(x):
    for y in x:
        random.randint(1,10)

####

#Main Tables
class Stud(UserMixin,db.Model):
    stud_id=db.Column(db.Integer, primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))

    def get_id(self): #Always ensure that get_id() returns a unique identifier for each user, 
                      #and that it's consistent with how your application retrieves users in the user loader callback.
        return str(self.stud_id)

class Prof(UserMixin,db.Model):
    prof_id=db.Column(db.Integer, primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))

    def get_id(self):
        return str(self.prof_id)

#----PASSING endpoints od eachpage and run functions
@app.route("/")
def homepage(): #main-page
    return render_template("first_page.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/home")
def home(): #home-page
    if Stud.is_authenticated or Prof.is_authenticated:         
        return render_template("home.html", pagetitle="Booking")
    else:
        return render_template("login.html",first_name=current_user.first_name) 
#--       
@app.route("/choose")
def choose():
    return render_template("choose.html",pagetitle="Choose")

@app.route("/error_message")
def error_message():
    return render_template("error_message.html",pagetitle="Choose")

@app.route("/signup_stud", methods=['POST','GET'])
def signup_stud():
    if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        uni_email=request.form.get('uni_email')
        password=request.form.get('password')
        uni=request.form.get('uni')
        faculty=request.form.get('faculty')
        depart=request.form.get('depart')
        gender=request.form.get('gender')
        type=request.form.get('Type')

        #Checks for duplicate emails
        user=Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
        user = not user
        flag = uni_email.endswith("@gmail.com") or uni_email.endswith("@hotmail.com") or uni_email.endswith("@outlook.com")
        st_pass = strong_pass(password)

        # Truth Table of 3 cases for -> valid mail, not used before, strong password 
        match(flag, user, st_pass):
            case (False, False, False) | (False, True, False): 
                return render_template("signup_stud.html", pop_message = "visible", pop_message1 = "visible", text = "Email is not valid")
            case (False, True, True) | (False, False, True): 
                return render_template("signup_stud.html", pop_message = "visible", pop_message1 = "hidden", text = "Email is not valid")
            case (True, False, False): 
                return render_template("signup_stud.html", pop_message = "visible", pop_message1 = "visible", text = "Email is already in use!")
            case (True, False, True): 
                return render_template("signup_stud.html", pop_message = "visible", pop_message1 = "hidden", text = "Email is already in use!")
            case (True, True, False): 
                return render_template("signup_stud.html", pop_message = "hidden", pop_message1 = "visible", text = "")
        
        #last case(valid case): continue sign-up
        
        #enhanced password: password is hashed(encrypted) in database to maintain security
        # encpassword=generate_password_hash(password) 
    #     #---SENDING DATA
        if type ==  "Student":
            new_user = Stud(first_name=first_name,
                            last_name=last_name,
                            uni_email=uni_email,
                            password=password,
                            uni=uni,
                            faculty=faculty,
                            depart=depart,
                            gender=gender)
        else:
            new_user = Prof(first_name=first_name,
                            last_name=last_name,
                            uni_email=uni_email,
                            password=password,
                            uni=uni,
                            faculty=faculty,
                            depart=depart,
                            gender=gender)

        db.session.add(new_user)
        db.session.commit()
        return render_template("login.html") #NOT EXECUTEDDDD
    return render_template('signup_stud.html',
                            pop_message = "hidden",
                            pop_message1 = "hidden",
                            text = "")

# @app.route("/signup_prof", methods=['POST','GET'])
# def signup_prof():
    
#     if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
#         first_name=request.form.get('first_name')
#         last_name=request.form.get('last_name')
#         uni_email=request.form.get('uni_email')
#         password=request.form.get('password')
#         uni=request.form.get('uni')
#         faculty=request.form.get('faculty')
#         depart=request.form.get('depart')
#         gender=request.form.get('gender')
#     #Checks for duplicate emails
#         prof=Prof.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
#         if prof:
#             flash("Email Already Exist","warning")
#             return render_template("signup_prof.html")
#             #enhanced password: password is hashed(encrypted) in database to maintain security
#             # encpassword=generate_password_hash(password) 
#             #---SENDING DATA
#         new_prof = Prof(first_name=first_name,
#                         last_name=last_name,
#                         uni_email=uni_email,
#                         password=password,
#                         uni=uni,
#                         faculty=faculty,
#                         depart=depart,
#                         gender=gender)
#         db.session.add(new_prof)
#         db.session.commit()
#         return render_template("login.html") #NOT EXECUTEDDDD
#     return render_template("signup_prof.html",pagetitle="Proof")

@app.route("/login", methods=['POST','GET'])
def login():
        if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
            uni_email=request.form.get('uni_email')
            password=request.form.get('password') 
            email_found= Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first()
            # pass_true=check_password_hash(email_found.password,password)
            
            if email_found and email_found.password==password:
                print("VALID")
                login_user(email_found)
                return redirect(url_for('home'))
                # return render_template("bookings.html")
            else:
                flash("Invalid Credendtials")
                print("INVALID CREDINTIALS")
                return render_template('login.html')    

        return render_template("login.html", pagetitle="Login")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication
