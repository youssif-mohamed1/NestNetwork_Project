from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin  
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import  login_user, logout_user,login_manager, LoginManager 
from flask_login import login_required, current_user
#sssssss
#My db connec
local_server=True
app=Flask(__name__) #creating object of class flask
app.secret_key='sasa'

# this for getting unique user access: unique page for each user:
login_manager=LoginManager(app) #idetifies the app that loginManager start to set policies for it
login_manager.login_view='Login' #specify the name of the view function (or the endpoint) that handles user logins. When an unauthorized user attempts..
                                 # ,to access a route or a resource that requires the user to be logged in.. 
                                 # ,Flask-Login automatically redirects the user to the URL associated with the view function specified in login_manager.login_view.
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#----DB CONNECTION:
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:username:password@localhost/database_table_name//' # Connection template line for database
#URL:https://www.example.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
#set some configuration values like the URL of the database, secret key, etc...
#--RETRIEVING DATA
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hnn' # username: root, password: blank, database_name: hms
db=SQLAlchemy(app) #creating object(Database) of class SQLALCHEMY



#Main Tables
class Stud(UserMixin,db.Model):
    stud_id=db.Column(db.Integer, primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50))
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))

class Prof(UserMixin,db.Model):
    prof_id=db.Column(db.Integer, primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50))
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))

#----PASSING endpoints od eachpage and run functions
@app.route("/")
def homepage(): #main-page
    return render_template("first_page.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/choose")
def choose():
    return render_template("choose.html",pagetitle="Choose")

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
        
        #Checks for duplicate emails
        stud=Stud.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
        if stud:
            flash("Email Already Exist","warning")
            return render_template("signup_stud.html")
        #enhanced password: password is hashed(encrypted) in database to maintain security
        # encpassword=generate_password_hash(password) 
        #---SENDING DATA
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
        return render_template("login.html") #NOT EXECUTEDDDD
    return render_template("signup_stud.html",pagetitle="Student")

@app.route("/signup_prof", methods=['POST','GET'])
def signup_prof():
    
    if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        uni_email=request.form.get('uni_email')
        password=request.form.get('password')
        uni=request.form.get('uni')
        faculty=request.form.get('faculty')
        depart=request.form.get('depart')
        gender=request.form.get('gender')
    
    #Checks for duplicate emails
        prof=Prof.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
        if prof:
            flash("Email Already Exist","warning")
            return render_template("signup_prof.html")
            #enhanced password: password is hashed(encrypted) in database to maintain security
            # encpassword=generate_password_hash(password) 
            #---SENDING DATA
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
        return render_template("login.html") #NOT EXECUTEDDDD
    return render_template("signup_prof.html",pagetitle="Proof")

@app.route("/login")
def login():
    return render_template("login.html",pagetitle="Login")


# @app.route("/logout")
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('Login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication
