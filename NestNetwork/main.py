from flask import Flask, render_template, request, session, redirect, url_for,flash,get_flashed_messages,jsonify
from flask_sqlalchemy import SQLAlchemy 
from flask_login import  UserMixin  
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import  login_user, logout_user,login_manager, LoginManager 
from flask_login import login_required, current_user
import random
import time
# from datetime import datetime
import smtplib
from email.message import EmailMessage
# import secrets
import string
# import json
#
###############------------##################

#My db connec and Login Handling
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
def communities(): #main-page
    return render_template("communities.html", pagetitle="Homepage") # Loading the HTML page

@app.route("/myaccount",methods=['POST','GET'])
def myaccount(): #main-page
    return render_template("myaccount.html", pagetitle="myaccount") # Loading the HTML page


@app.route("/home", methods=['POST','GET'])
def home(): #main-page
    return render_template("home.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page

@app.route("/home_loggedin", methods=['POST','GET'])
def home_loggedin(): #main-page
    return render_template("home_loggedin.html", pagetitle="Homepage", logged = "logged-no" ) # Loading the HTML page


@app.route("/contact",methods=['POST','GET'])
def contact(): #main-page
    return render_template("contact.html", pagetitle="Contactpage") # Loading the HTML page

@app.route("/about",methods=['POST','GET'])
def about(): #main-page
    return render_template("about.html", pagetitle="Aboutpage") # Loading the HTML page

@app.route("/ps",methods=['POST','GET'])
def ps():
    return render_template("ps.html")


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
        global flash_flag_newpass
        if flash_flag_newpass:
            flash("New password sent")
        if request.method=="POST":  #Checking IF Submit button(signup) is pressed ('action' is activated)
            uni_email=request.form.get('uni_email')
            password=request.form.get('password') 
            email_found= Stud.query.filter_by(uni_email=uni_email).first() or Prof.query.filter_by(uni_email=uni_email).first()
            # pass_true=check_password_hash(email_found.password,password)
            
            if email_found and email_found.password==password:
                #print("VALID")
                login_user(email_found)
                return render_template("home_loggedin.html", logged = "logged-yes")
                #return redirect(url_for('homepage')) #redirect is same as render but its used to: avoid resumbissions  
                                                     # Instead of sending a response that could result in a duplicated POST if the user refreshes the page,
                                                     # the server redirects the user to /HOME USED IN SIGNUP MORE LIKELY OR ANY RECORDING DATABASE PROCESSES
            else:
                return render_template('login.html', logged = "logged-no")    

        return render_template("login.html", pagetitle="Login", logged = "logged-no")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True, port=5000) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication
