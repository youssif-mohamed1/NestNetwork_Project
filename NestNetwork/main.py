from flask import Flask, render_template, request, session, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin  
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import  login_user, logout_user,login_manager, LoginManager 
from flask_login import login_required, current_user
import random
from datetime import datetime
import smtplib
from email.message import EmailMessage
# import json
#---
#HELLO WORLD
#sssssss yoyoyoyoyoyoyoyoyo 2134
#My db connec
#dsfs
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
    user=Stud.query.get(str(user_id))
    if user is None:
        user=Prof.query.get(str(user_id))
    return user
#
#----DB CONNECTION:
# app.config['SQLALCHEMY_DATABASE_URI']='mysql:username:password@localhost/database_table_name//' # Connection template line for database
#URL:https://www.example.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
#set some configuration values like the URL of the database, secret key, etc...
#--RETRIEVING DATA
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hnn' # username: root, password: blank, database_name: hms
db=SQLAlchemy(app) #creating object(Database) of class SQLALCHEMY

#####

#Main Tables
class Stud(UserMixin,db.Model):
    stud_id=db.Column(db.String(50), primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    ph_num=db.Column(db.String(50))

    def get_id(self): #Always ensure that get_id() returns a unique identifier for each user, 
                      #and that it's consistent with how your application retrieves users in the user loader callback.
        return str(self.stud_id)

class Prof(UserMixin,db.Model):
    prof_id=db.Column(db.String(50), primary_key=True) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    ph_num=db.Column(db.String(50),unique=True)

    def get_id(self):
        return str(self.prof_id)
####

#-----functions block

#1-->pass_vald
def strong_pass(password):
    return len(password) >=8 and len(password) <=20 and any(char.isupper() for char in password) and not password.isalnum() and any(char.islower() for char in password) and any(char.isdigit() for char in password)

#2-->rand_id
def rand_id(x):
    rand_no=random.randint(1000,2000)
    if x=="Professor":
        return "pf"+str(rand_no)    
    else: return "st" + str(rand_no)

#3--> forgot_pass
done=False
def forgot_password(x_email):
    global done
    # if session.get('message_sent', False):
    #     return
    if done:
        return
    # ph_num = x_phone
    # user_phone =Stud.query.filter_by(ph_num=ph_num).first()
    # if user_phone is None:
    #     user_phone=Prof.query.filter_by(ph_num=ph_num).first()

    uni_email=x_email
    user_email =Stud.query.filter_by(uni_email=uni_email).first()
    if user_email is None:
        user_email=Prof.query.filter_by(uni_email=uni_email).first()
    
    user_name="None"
    if user_email:
        user_name=user_email.first_name +" "+user_email.last_name
    
    #Verification_Code
    verf_codes=[]
    rand_code=random.randint(100000,900000)
    while rand_code in verf_codes:
        rand_code=random.randint(100000,900000)
    verf_codes.append(rand_code)            
    # print(user_name)
    if user_email :
        email_alert("Verification Code", f"hello {user_name}, This the Verification Code: {rand_code}","moustafaalaa30@gmail.com" )
        flash("Verification message sent to your email")
        done=True
    elif x_email:
        flash("Email not found")
    # session['message_sent'] = True 

#3-->Send Message
def email_alert(subject, body, to):
    msg=EmailMessage()
    msg.set_content(body)
    msg['subject']=subject
    msg['to']=to
    admin="nestnetworkhelwan@gmail.com"
    msg['from']=admin
    password="yntwpbzneechjelp"
    server=smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls() # (Secure Socket Layer/Transport Layer Security), provide secure connection
    server.login(admin, password)
    server.send_message(msg)
    
    server.quit()
# Usage
# send_email_to_sms('1234567890', 'txt.att.net', 'Test SMS via Email', 'Hello, this is a test message sent via email!')
####


#----PASSING endpoints of eachpage and run functions
@app.route("/")
def homepage(): #main-page
    return render_template("home.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/ps",methods=['POST','GET'])
def ps():
    return render_template("ps.html")

@app.route("/signup", methods=['POST','GET'])
def signup():
    if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
        first_name=request.form.get('first_name')
        last_name=request.form.get('last_name')
        uni_email=request.form.get('uni_email')
        password=request.form.get('password')
        uni=request.form.get('uni')
        faculty=request.form.get('faculty')
        depart=request.form.get('depart')
        gender=request.form.get('gender')
        ph_num=request.form.get('ph_num')
        type=request.form.get('Type')
#--
        #Unique_ID:
        gen_id=1
        while(gen_id):
            ruser_id=rand_id(type)
            gen_id=Stud.query.filter_by(stud_id=ruser_id).first() or Prof.query.filter_by(prof_id=ruser_id).first() #authinticate if the email entered already exist
            

        #Checks for duplicate emails
        user=Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
        user = not user
        flag = uni_email.endswith("@gmail.com") or uni_email.endswith("@hotmail.com") or uni_email.endswith("@outlook.com")
        st_pass = strong_pass(password)

        # Truth Table of 3 cases for -> valid mail, not used before, strong password 
        match(flag, user, st_pass):
            case (False, False, False) | (False, True, False): 
                return render_template("signup.html", pop_message = "visible", pop_message1 = "visible", text = "Email is not valid")
            case (False, True, True) | (False, False, True): 
                return render_template("signup.html", pop_message = "visible", pop_message1 = "hidden", text = "Email is not valid")
            case (True, False, False): 
                return render_template("signup.html", pop_message = "visible", pop_message1 = "visible", text = "Email is already in use!")
            case (True, False, True): 
                return render_template("signup.html", pop_message = "visible", pop_message1 = "hidden", text = "Email is already in use!")
            case (True, True, False): 
                return render_template("signup.html", pop_message = "hidden", pop_message1 = "visible", text = "")
        
        #last case(valid case): continue sign-up
        
        #enhanced password: password is hashed(encrypted) in database to maintain security
        # encpassword=generate_password_hash(password) 
        #---SENDING DATA
        if type ==  "Student":
            new_user = Stud(stud_id=ruser_id,
                            first_name=first_name,
                            last_name=last_name,
                            uni_email=uni_email,
                            password=password,
                            uni=uni,
                            faculty=faculty,
                            depart=depart,
                            gender=gender,
                            ph_num=ph_num)
        else:
            new_user = Prof(prof_id=ruser_id,
                            first_name=first_name,
                            last_name=last_name,
                            uni_email=uni_email,
                            password=password,
                            uni=uni,
                            faculty=faculty,
                            depart=depart,
                            gender=gender,
                            ph_num=ph_num)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
        # return render_template("login.html") #NOT EXECUTEDDDD
    return render_template('signup.html',
                            pop_message = "hidden",
                            pop_message1 = "hidden",
                            text = "")

@app.route("/vref", methods=['POST','GET'])
def vref():
    uni_email=request.form.get('uni_email')
    # ph_num=request.form.get('ph_num')
    forgot_password(uni_email)
    return render_template ("vref.html")


@app.route("/login", methods=['POST','GET'])
def login():
        if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
            uni_email=request.form.get('uni_email')
            password=request.form.get('password') 
            email_found= Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first()
            # pass_true=check_password_hash(email_found.password,password)
            
            if email_found and email_found.password==password:
                # print("VALID")
                login_user(email_found)
                return redirect(url_for('homepage')) #redirect is same as render but its used to: avoid resumbissions  
                                                     # Instead of sending a response that could result in a duplicated POST if the user refreshes the page,
                                                     # the server redirects the user to /HOME USED IN SIGNUP MORE LIKELY OR ANY RECORDING DATABASE PROCESSES
                # return render_template("home.html")
            else:
                # flash("Invalid Credendtials")
                # print("INVALID CREDINTIALS")
                return render_template('login.html')    

        return render_template("login.html", pagetitle="Login")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication
