from flask import Flask, render_template, request, session, redirect, url_for,flash,get_flashed_messages,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin  
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import  login_user, logout_user,login_manager, LoginManager 
from flask_login import login_required, current_user
import random
import time
import atexit
# from datetime import datetime
import smtplib
from email.message import EmailMessage
# import secrets
import string
# import json
##
###############------------##################

#My db connec and Login Handling
#dsfs
local_server=True
app=Flask(__name__) #creating object of class flask
app.secret_key='sasa'
#
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
<<<<<<< HEAD
# URL:https://w...content-available-to-author-only...e.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
# set some configuration values like the URL of the database, secret key, etc...
# --RETRIEVING DATA
# username: root, password: blank, database_name: hms
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/hnn'
db = SQLAlchemy(app)  # creating object(Database) of class SQLALCHEMY
=======
#URL:https://www.example.com/path/to/file (must be locator) // URI:urn:isbn:0451450523 (CAN be name or loactor)
#set some configuration values like the URL of the database, secret key, etc...
#--RETRIEVING DATA
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/hnn' # username: root, password: blank, database_name: hms
db=SQLAlchemy(app) #creating object(Database) of class SQLALCHEMY
>>>>>>> 67d0afa729459fd700a5cee74e2e03a72535cab6

###############------------##################

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

<<<<<<< HEAD

class problem_solving(UserMixin, db.Model):

    no = db.Column(db.Integer, primary_key=True)
    topic_name = db.Column(db.String(50))  # Defining Attributes
    level = db.Column(db.String(50))
    video = db.Column(db.String(50))
    sheet = db.Column(db.String(50))

    def get_id(self):  # Always ensure that get_id() returns a unique identifier for each user,
        # and that it's consistent with how your application retrieves users in the user loader callback.
        return str(self.no)


class Login(UserMixin, db.Model):
    number = db.Column(db.String(50), primary_key=True)
    id = db.Column(db.String(50))  # Defining Attributes
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    uni_email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(50))
    uni = db.Column(db.String(50))
    faculty = db.Column(db.String(50))
    depart = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    ph_num = db.Column(db.String(50))
=======
class problem_solving(UserMixin,db.Model):
    
    no = db.Column(db.Integer, primary_key=True)
    topic_name=db.Column(db.String(50)) #Defining Attributes
    level=db.Column(db.String(50))
    video=db.Column(db.String(50))
    sheet=db.Column(db.String(50))

    def get_id(self): #Always ensure that get_id() returns a unique identifier for each user, 
                      #and that it's consistent with how your application retrieves users in the user loader callback.
        return str(self.no)

class Login(UserMixin,db.Model):
    number=db.Column(db.String(50), primary_key=True)
    id=db.Column(db.String(50)) #Defining Attributes
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    uni_email=db.Column(db.String(50), unique=True)
    password=db.Column(db.String(50))
    uni=db.Column(db.String(50))
    faculty=db.Column(db.String(50))
    depart=db.Column(db.String(50))
    gender=db.Column(db.String(50))
    ph_num=db.Column(db.String(50))
>>>>>>> 67d0afa729459fd700a5cee74e2e03a72535cab6
    type = db.Column(db.String(50))
    def get_id(self): #Always ensure that get_id() returns a unique identifier for each user, 
                      #and that it's consistent with how your application retrieves users in the user loader callback.
        return str(self.id)

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

class Contests(UserMixin,db.Model):
    Contest_name=db.Column(db.String(50)) #Defining Attributes
    Contest_link=db.Column(db.String(50))
    Contest_filter=db.Column(db.String(50))
    Contest_key=db.Column(db.String(50))
    web_site=db.Column(db.String(50))
    number=db.Column(db.String(50), primary_key=True)

    def get_id(self):
        return str(self.number)

class Problem_solving_community_users(UserMixin,db.Model):
    cf_handle = db.Column(db.String(50), primary_key=True)
    vj_handle = db.Column(db.String(50))
    id = db.Column(db.String(50))

    def get_id(self):
        return str(self.cf_handle)
###############------------##################

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
email_global="NONE"
name_global="NONE"
id_global=""
rand_code_global=0
rand_pass_global=""
flash_flag_resend=False
flash_flag_newpass=False

def forgot_password(x_email):
    global done
    global email_global
    global name_global
    global rand_code_global
    global id_global
    # print(done)
    uni_email=x_email
    flag=True
    user_email =Stud.query.filter_by(uni_email=uni_email).first()
    if user_email is not None: id_global=user_email.stud_id
    if user_email is None:
        user_email=Prof.query.filter_by(uni_email=uni_email).first()
        if user_email is not None: id_global=user_email.prof_id
    # if user_email is None: flag=False
    if done:
        # if flag:
        #     flash("You can resend your email again now")
        # else:
        #     flash("Email not found")
        # while 1:
        #     time.sleep(3)
        #     done=False
        #     return
        return
    # ph_num = x_phone
    # user_phone =Stud.query.filter_by(ph_num=ph_num).first()
    # if user_phone is None:
    #     user_phone=Prof.query.filter_by(ph_num=ph_num).first()
   
    user_name="None"
    if user_email:
        user_name=user_email.first_name +" "+user_email.last_name
    
    #Verification_Code
    vref_codes=[]
    rand_code=random.randint(100000,900000)
    while rand_code in vref_codes:
        rand_code=random.randint(100000,900000)
    vref_codes.append(rand_code)            
    
    rend_page="" #the page that will be rendered (confirm_vcode or vref)
    if user_email :   

        #passing variables to all functions   
        email_global=user_email
        name_global=user_name
        rand_code_global=rand_code

        #sending the message
        email_alert("Verification Code", f"Hello {user_name}, This the Verification Code: {rand_code}","moustafaalaa30@gmail.com" )
        done=True
        rend_page="confirm_vcode"
    
    elif x_email:
        rend_page="vref"    
        flash("Email not found")
    
    return rend_page
#3-->Generate Strong Pass:
# define the characters that can be used in the password
def generate_random_pass():
    all_characters = string.ascii_letters + string.digits + string.punctuation
    length = 10

    # generate a password using randomly chosen characters
    # using the 'choices' function from the random module
    # and joining the resulting characters into a string
    password = ''.join(random.choices(all_characters, k=length)) #is an built-in variable in function choice(left-click+ctrl: to see)
                                                                 #all_char: is sent to variable named population that ensures strong pass
    return password

#4-->Send Message
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

#
#5--> Update DATABASE
def update_user(user_id,
                first_name,
                last_name,
                uni_email,
                password,
                uni,
                faculty,
                depart,
                gender,
                ph_num ):
    # global rand_pass_global #temp
    # Find user by ID
    user = Stud.query.get(user_id)
    if user is None: 
        user=Prof.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    # Update fields from request data
    if first_name != "":
        user.first_name=first_name
    if last_name != "":
        user.last_name=last_name
    if uni_email != "":
        user.uni_email=uni_email
    if uni != "":
        user.uni=uni
    if faculty != "":
        user.faculty=faculty
    if depart != "":
        user.depart=depart
    if gender != "":
        user.genderm=gender
    if ph_num != "":
        user.ph_num=ph_num
    if password:
        user.password = password
    # Commit changes to database
    db.session.commit()
    return jsonify({"success": "User updated successfully", "user": str(user)})
###############------------##################


#----PASSING endpoints of eachpage and run functions
@app.route("/")
def homepage(): #main-page
    return render_template("home.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/communities", methods=['POST','GET'])
def communities(): 
    return render_template("communities.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/myaccount",methods=['POST','GET'])
def myaccount(): 
    return render_template("myaccount.html", pagetitle="myaccount") # Loading the HTML page


@app.route("/home", methods=['POST','GET'])
def home(): 
    return render_template("home.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/home_loggedin", methods=['POST','GET'])
def home_loggedin(): 
    return render_template("home_loggedin.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/about_loggedin", methods=['POST','GET'])
def about_loggedin(): 
    return render_template("about_loggedin.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/contact_loggedin", methods=['POST','GET'])
def contact_loggedin(): 
    return render_template("contact_loggedin.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/communities_loggedin", methods=['POST','GET'])
def communities_loggedin(): 
    return render_template("communities_loggedin.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/contact",methods=['POST','GET'])
def contact(): 
    return render_template("contact.html", pagetitle="Contactpage") # Loading the HTML page

@app.route("/about",methods=['POST','GET'])
def about(): 
    return render_template("about.html", pagetitle="Aboutpage") # Loading the HTML page

<<<<<<< HEAD

@app.route("/about_loggedin", methods=['POST', 'GET'])
def about_loggedin():  # main-page
    # Loading the HTML page
    return render_template("about_loggedin.html", pagetitle="Homepage", logged="logged-no")


@app.route("/contact_loggedin", methods=['POST', 'GET'])
def contact_loggedin():  # main-page
    # Loading the HTML page
    return render_template("contact_loggedin.html", pagetitle="Homepage", logged="logged-no")


@app.route("/communities_loggedin", methods=['POST', 'GET'])
def communities_loggedin():  # main-page
    # Loading the HTML page
    return render_template("communities_loggedin.html", pagetitle="Homepage", logged="logged-no")


@app.route("/contact", methods=['POST', 'GET'])
def contact():  # main-page
    # Loading the HTML page
    return render_template("contact.html", pagetitle="Contactpage")


@app.route("/about", methods=['POST', 'GET'])
def about():  # main-page
    # Loading the HTML page
    return render_template("about.html", pagetitle="Aboutpage")

=======
@app.route("/ps_intro", methods=['POST','GET'])
def ps_intro(): 
    return render_template("ps_intro.html", pagetitle="ps_intro", logged = "logged-no" ) # Loading the HTML page

@app.route("/ps_intro_loggedin", methods=['POST','GET'])
def ps_intro_loggedin(): 
    return render_template("ps_intro_loggedin.html", pagetitle="ps_intro_loggedin", logged = "logged-no" ) # Loading the HTML page
>>>>>>> 67d0afa729459fd700a5cee74e2e03a72535cab6

#####################################################################################

##


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
            

<<<<<<< HEAD
        # Checks for duplicate emails
        user = Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(
            uni_email=uni_email).first()  # authinticate if the email entered already exist
        user = not user  # if there a duplicate
        flag = uni_email.endswith("@gmail.com") or uni_email.endswith(
            "@hotmail.com") or uni_email.endswith("@outlook.com")
        # email valid
        st_pass = strong_pass(password)
        # strong pass

        # Truth Table of 3 cases for -> valid mail, not used before, strong password
=======
        #Checks for duplicate emails
        user=Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first() #authinticate if the email entered already exist
        user = not user # if there a duplicate
        flag = uni_email.endswith("@gmail.com") or uni_email.endswith("@hotmail.com") or uni_email.endswith("@outlook.com")
        # email valid
        st_pass = strong_pass(password)
        #strong pass
        
        # Truth Table of 3 cases for -> valid mail, not used before, strong password 
>>>>>>> 67d0afa729459fd700a5cee74e2e03a72535cab6
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
        
        #---SENDING Records to the DATABASE
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

#####################################################################################
@app.route("/confirm_vcode", methods=['POST','GET'])
def confirm_vcode():
    global rand_code_global
    global rand_pass_global
    global id_global
    global flash_flag_newpass
    global flash_flag_resend
    cur_func="confirm_vcode"

    flash("Verification message sent to your email, click Resend if not sent")

    # #check that id_global to is in database //just double_check that sent id is in the database
    # user = Stud.query.filter_by(stud_id=id_global)
    # user_id=user.stud_id
    # if user is None: 
    #     user=Prof.query.filter_by(prof_id=id_global)
    #     user_id=user.prof_id


    #generate random strong pass
    vref_code=""
    vref_code=request.form.get('vref_code')
    rand_passes=[]
    rand_pass=generate_random_pass()
    while rand_pass in rand_passes:
        rand_pass=generate_random_pass()
    rand_passes.append(rand_pass)
    
    #check for verification code
    if vref_code==str(rand_code_global):
        rand_pass_global=rand_pass
        # print("Right Verf_code")
        update_user(user_id=id_global,
                first_name="",
                last_name="",
                uni_email="",
                password=rand_pass,
                uni="",
                faculty="",
                depart="",
                gender="",
                ph_num="")
        email_alert("Password Reset", f"Hello {name_global}, This is your new password: {rand_pass}", "moustafaalaa30@gmail.com")
        print("Password Sent")
        flash_flag_newpass=True
        get_flashed_messages()
        return redirect(url_for('login'))
    elif vref_code:
        flash("Verification code is wrong")
    return render_template ("confirm_vcode.html")

#resend_hyperlink(in confirm_vcode) function
@app.route('/handle_resend')
def handle_resend():
    global rand_code_global
    global name_global
    global flash_flag_resend
    flash_flag_resend=True

    email_alert("Verification Code", f"Hello {name_global}, This the Verification Code: {rand_code_global}","moustafaalaa30@gmail.com" )
    return redirect(url_for("confirm_vcode"))  # Redirecting

@app.route("/vref", methods=['POST','GET'])
def vref():
    uni_email=request.form.get('uni_email')
    # ph_num=request.form.get('ph_num')
    rend_page=""
    rend_page=forgot_password(uni_email)
    if rend_page=="" : rend_page="vref"
    if rend_page !="vref": return redirect(url_for("confirm_vcode"))
    return render_template ("vref.html")


@app.route("/login", methods=['POST','GET'])
def login():
<<<<<<< HEAD
    global flash_flag_newpass
    if flash_flag_newpass:
        flash("New password sent")
    # Checking IF Submit button(signup) is pressed ('action' is activated)
    if request.method == "POST":
        uni_email = request.form.get('uni_email')
        password = request.form.get('password')
        email_found = Stud.query.filter_by(uni_email=uni_email).first()
        if email_found and email_found.password == password:
            login_user(email_found)
            new_user = Login(
                number='1',
                id=email_found.stud_id,
                first_name=email_found.first_name,
                last_name=email_found.last_name,
                uni_email=email_found.uni_email,
                password=email_found.password,
                uni=email_found.uni,
                faculty=email_found.faculty,
                depart=email_found.depart,
                gender=email_found.gender,
                ph_num=email_found.ph_num,
                type="Student"
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template("home_loggedin.html", logged="logged-yes")
            # return redirect(url_for('homepage')) #redirect is same as render but its used to: avoid resumbissions
            # Instead of sending a response that could result in a duplicated POST if the user refreshes the page,
            # the server redirects the user to /HOME USED IN SIGNUP MORE LIKELY OR ANY RECORDING DATABASE PROCESSES

        email_found = Prof.query.filter_by(uni_email=uni_email).first()
        if email_found and email_found.password == password:
            new_user = Login(
                number='1',
                id=email_found.prof_id,
                first_name=email_found.first_name,
                last_name=email_found.last_name,
                uni_email=email_found.uni_email,
                password=email_found.password,
                uni=email_found.uni,
                faculty=email_found.faculty,
                depart=email_found.depart,
                gender=email_found.gender,
                ph_num=email_found.ph_num,
                type="Proffesor"
            )
            db.session.add(new_user)
            db.session.commit()
            return render_template("home_loggedin.html", logged="logged-yes")

    return render_template("login.html", pagetitle="Login", logged="logged-no")


@app.route("/myaccount_loggedin", methods=['POST', 'GET'])
=======
        global flash_flag_newpass
        if flash_flag_newpass:
            flash("New password sent")
        if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
            uni_email=request.form.get('uni_email')
            password=request.form.get('password') 
            email_found= Stud.query.filter_by(uni_email=uni_email).first() 
            if email_found and email_found.password==password:
                login_user(email_found)
                new_user = Login(
                                number = '1',
                                id = email_found.stud_id,
                                first_name=email_found.first_name,
                                last_name=email_found.last_name,
                                uni_email=email_found.uni_email,
                                password=email_found.password,
                                uni=email_found.uni,
                                faculty=email_found.faculty,
                                depart=email_found.depart,
                                gender=email_found.gender,
                                ph_num=email_found.ph_num,
                                type = "Student"
                                )
                db.session.add(new_user)
                db.session.commit()
                return render_template("home_loggedin.html", logged = "logged-yes")
                #return redirect(url_for('homepage')) #redirect is same as render but its used to: avoid resumbissions  
                                                     # Instead of sending a response that could result in a duplicated POST if the user refreshes the page,
                                                     # the server redirects the user to /HOME USED IN SIGNUP MORE LIKELY OR ANY RECORDING DATABASE PROCESSES
            
            email_found = Prof.query.filter_by(uni_email=uni_email).first()
            if email_found and email_found.password==password:
                new_user = Login(
                                number = '1',
                                id = email_found.prof_id,
                                first_name=email_found.first_name,
                                last_name=email_found.last_name,
                                uni_email=email_found.uni_email,
                                password=email_found.password,
                                uni=email_found.uni,
                                faculty=email_found.faculty,
                                depart=email_found.depart,
                                gender=email_found.gender,
                                ph_num=email_found.ph_num,
                                type = "Proffesor"
                                )
                db.session.add(new_user)
                db.session.commit()
                return render_template("home_loggedin.html", logged = "logged-yes")
            
        return render_template("login.html", pagetitle="Login", logged = "logged-no")

@app.route("/myaccount_loggedin", methods=['POST','GET'])
>>>>>>> 67d0afa729459fd700a5cee74e2e03a72535cab6
def myaccount_loggedin():
    account = Login.query.filter_by(number='1').first()
    return render_template("myaccount_loggedin.html",
                            pagetitle="account_loggedin",
                            fname = account.first_name,
                            lname = account.last_name,
                            email = account.uni_email,
                            ph_num = account.ph_num,
                            type = account.type,
                            uni = account.uni,
                            gend = account.gender,
                            faclt = account.faculty,
                            depart = account.depart) # Loading the HTML pagep

@app.route("/logout")
@login_required
def logout():
    user = Login.query.get('1')
    db.session.delete(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('login'))
@app.route("/save_data",methods = ['POST', 'GET'])
def save_data():
    # data = request.json
    photo=request.form.get('photo')
    first_name=request.form.get('first_name')
    last_name=request.form.get('last_name')
    uni=request.form.get('uni')
    faculty=request.form.get('faculty')
    depart=request.form.get('depart')
    gender=request.form.get('gender')
    ph_num=request.form.get('ph_num')
    user_loggedin = Login.query.filter_by(number = '1').first()
    user = Stud.query.filter_by(stud_id=user_loggedin.id).first()
    print(first_name)
    if user is None:
        user = Prof.query.filter_by(prof_id=user_loggedin.id).first()    
    if user:
        update_user(user_id = user_loggedin.id,
                    first_name = first_name,
                    last_name = last_name,
                    uni_email = user_loggedin.uni_email,
                    password = user.password,
                    uni = uni,
                    faculty = faculty,
                    depart = depart,
                    gender = gender,
                    ph_num = ph_num)
        user1 = Login.query.get('1')
        db.session.delete(user1)
        new_user = Login(
                        number = '1',
                        id = user_loggedin.id,
                        first_name=first_name,
                        last_name=last_name,
                        uni_email=user_loggedin.uni_email,
                        password=user.password,
                        uni=uni,
                        faculty=faculty,
                        depart=depart,
                        gender=gender,
                        ph_num=ph_num,
                        type = user_loggedin.type
                        )
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('myaccount_loggedin', message='hidden', text='saved'))
    return redirect(url_for('myaccount_loggedin', message='hidden', text='saved'))
    
# def cleanup_database():
#     print("OUT")
#     db.session.delete(Login.query.get('1'))
#     db.session.commit()

@app.route("/edit_account",methods=['POST','GET'])
def edit_account():
    account = Login.query.filter_by(number='1').first()
    return render_template("edit_account.html",
                            pagetitle="edit_account",
                            fname = account.first_name,
                            lname = account.last_name,
                            email = account.uni_email,
                            ph_num = account.ph_num,
                            type = account.type,
                            uni = account.uni,
                            gend = account.gender,
                            faclt = account.faculty,
                            depart = account.depart)
#####################################################################################################

@app.route("/signup_for_ps", methods=['POST','GET'])
def signup_for_ps(): #main-page
    cf_handle = request.form.get('cf_handle')
    vj_handle = request.form.get('vj_handle')
    if cf_handle is None or vj_handle is None:
        return render_template("signup_for_ps.html", pagetitle="ps", popmessage = "hidden", message = "")
    else:
        user = Problem_solving_community_users.query.filter_by(cf_handle=cf_handle).first()
        if user:
            if vj_handle == user.vj_handle:
                return redirect(url_for("ps")) # Loading the HTML page
            else:
                return render_template("signup_for_ps.html", pagetitle="ps", popmessage = "visible", message = "Wrong Vjudge handle") # Loading the HTML page
        else:
            user2 = Problem_solving_community_users.query.filter_by(vj_handle=vj_handle).first()
            if user2:
                return render_template("signup_for_ps.html", pagetitle="ps", popmessage = "visible", message = "Vjudge handle is already used")
        new_user = Problem_solving_community_users(
                                                    cf_handle = cf_handle,
                                                    vj_handle = vj_handle,
                                                    id = Login.query.filter_by(number = '1').first().id
                                                    ); 
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("ps"))

@app.route("/ps_div1",methods=['POST','GET'])
def ps_div1():
    div1 = Contests.query.filter_by(Contest_filter="Div. 1").all() 
    return render_template("ps_div.html", pagetitle="ps_divpage", div = div1 , message = "Div 1") 

@app.route("/ps_div2",methods=['POST','GET'])
def ps_div2(): 
    div2 = Contests.query.filter_by(Contest_filter="Div. 2").all()
    return render_template("ps_div.html", pagetitle="ps_divpage", div = div2 , message = "Div 2") 

@app.route("/ps_div3",methods=['POST','GET'])
def ps_div3(): 
    div3 = Contests.query.filter_by(Contest_filter="Div. 3").all()
    return render_template("ps_div.html", pagetitle="ps_divpage", div = div3 , message = "Div 3") 

@app.route("/ps_div4",methods=['POST','GET'])
def ps_div4(): 
    div4 = Contests.query.filter_by(Contest_filter="Div. 4").all()
    return render_template("ps_div.html", pagetitle="ps_divpage", div = div4 , message = "Div 4") 

@app.route("/ps_other",methods=['POST','GET'])
def ps_div5(): 
    other = Contests.query.filter(Contests.Contest_filter.is_(None)).all()
    return render_template("ps_div.html", pagetitle="ps_divpage", div = other , message = "Others") 


@app.route("/ps", methods=['POST', 'GET'])
def ps():
    mat = []
    for i in range(4):  # i == 0
        row = {}
        lev1 = problem_solving.query.filter_by(level=str(i)).all()
        lev = [(problem_solving.topic_name, problem_solving.video,
                problem_solving.sheet) for problem_solving in lev1]
        if lev:
            for item in lev:
                topic_name, videos, sheets = item
                if topic_name in row:
                    row[topic_name].append((videos, sheets))
                else:
                    row[topic_name] = [(videos, sheets)]
        mat.append(row)

    li = []
    for idx, row2 in enumerate(mat):
        for topic, data in row2.items():
            li1 = []
            li2 = []
            for videos, sheets in data:
                li1.append(videos)
                li2.append(sheets)
            li.append(li1)
            li.append(li2)

<<<<<<< HEAD
    return render_template("ps.html",
                           link010=li[0], link011=li[1], link020=li[2], link021=li[3], link030=li[4], link031=li[5], link040=li[6], link041=li[7], link050=li[8], link051=li[9], link060=li[10], link061=li[11], link070=li[12], link071=li[13], link080=li[14], link081=li[15], link090=li[16], link091=li[17])
    # link100 = li[18],
    # link101 = li[19],
    # link110 = li[20],
    # link111 = li[21],
    # link120 = li[22],
    # link121 = li[23],
    # link130 = li[24],
    # link131 = li[25],
    # link140 = li[26],
    # link141 = li[27],
    # link150 = li[28],
    # link151 = li[29],
    # link160 = li[30],
    # link161 = li[31],
    # link200 = li[32],
    # link201 = li[33],
    # link210 = li[34],
    # link211 = li[35],
    # link220 = li[36],
    # link221 = li[37],
    # link230 = li[38],
    # link231 = li[39],
    # link240 = li[40],
    # link241 = li[41],
    # link250 = li[42],
    # link251 = li[43],
    # link260 = li[44],
    # link261 = li[45],
    # link270 = li[46],
    # link271 = li[47],
    # link280 = li[48],
    # link281 = li[49],
    # link290 = li[50],
    # link291 = li[51],
    # link300 = li[52],
    # link301 = li[53],
    # link310 = li[55],
    # link311 = li[56],
    # link320 = li[57],
    # link321 = li[58],
    # link330 = li[59],
    # link331 = li[60],
    # link340 = li[61],
    # link341 = li[62],
    # link350 = li[63],
    # link351 = li[64],
    # link360 = li[65],
    # link361 = li[66],
    # link370 = li[67],
    # link371 = li[68],
    # link380 = li[69],
    # link381 = li[70],
    # link390 = li[71],
    # link391 = li[72])

=======
    return render_template("ps.html" ,
                            link010 = li[0],link011 = li[1],link020 = li[2],link021 = li[3],link030 = li[4],link031 = li[5],link040 = li[6],link041 = li[7],link050 = li[8],link051 = li[9],link060 = li[10],link061 = li[11],link070 = li[12],link071 = li[13],link080 = li[14],link081 = li[15],link090 = li[16],link091 = li[17]
                            )
                            
                            # link100 = li[18],
                            # link101 = li[19],
                            # link110 = li[20],
                            # link111 = li[21],
                            # link120 = li[22],
                            # link121 = li[23],
                            # link130 = li[24],
                            # link131 = li[25],
                            # link140 = li[26],
                            # link141 = li[27],
                            # link150 = li[28],
                            # link151 = li[29],
                            # link160 = li[30],
                            # link161 = li[31],
                            # link200 = li[32],
                            # link201 = li[33],
                            # link210 = li[34],
                            # link211 = li[35],
                            # link220 = li[36],
                            # link221 = li[37],
                            # link230 = li[38],
                            # link231 = li[39],
                            # link240 = li[40],
                            # link241 = li[41],
                            # link250 = li[42],
                            # link251 = li[43],
                            # link260 = li[44],
                            # link261 = li[45],
                            # link270 = li[46],
                            # link271 = li[47],
                            # link280 = li[48],
                            # link281 = li[49],
                            # link290 = li[50],
                            # link291 = li[51],
                            # link300 = li[52],
                            # link301 = li[53],
                            # link310 = li[55],
                            # link311 = li[56],
                            # link320 = li[57],
                            # link321 = li[58],
                            # link330 = li[59],
                            # link331 = li[60],
                            # link340 = li[61],
                            # link341 = li[62],
                            # link350 = li[63],
                            # link351 = li[64],
                            # link360 = li[65],
                            # link361 = li[66],
                            # link370 = li[67],
                            # link371 = li[68],
                            # link380 = li[69],
                            # link381 = li[70],
                            # link390 = li[71],
                            # link391 = li[72])
>>>>>>> 46f2cc91340aac4bd6aa1d0b77c417d617e01595


# atexit.register(cleanup_database)
if __name__ == "__main__":
    app.run(debug=True, port=5000) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication