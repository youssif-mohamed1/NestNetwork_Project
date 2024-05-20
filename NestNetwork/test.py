# from flask import Flask, render_template, request, session, redirect, url_for,flash,get_flashed_messages,jsonify
# from flask_sqlalchemy import SQLAlchemy 
# from flask_login import  UserMixin  
# from werkzeug.security import generate_password_hash,check_password_hash
# from flask_login import  login_user, logout_user,login_manager, LoginManager 
# from flask_login import login_required, current_user
# import random
# import requests
# from bs4 import BeautifulSoup
# import time
# import atexit
# from datetime import datetime
# import smtplib
# from email.message import EmailMessage
# # import secrets
# import string
# local_server=True
# app=Flask(__name__) #creating object of class flask
# app.secret_key='sasa'
# app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:@localhost/redit' # username: root, password: blank, database_name: hms
# db=SQLAlchemy(app) #creating object(Database) of class SQLALCHEMY

# class Posts(UserMixin,db.Model):
#     order= db.Column(db.Integer, unique=True)
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100)) 
#     content = db.Column(db.Text )
#     date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

#     # replies = db.relationship('Reply', backref='post', lazy=True)

# # class Reply(db.Model):
# #     ord= db.Column(db.Integer, unique=True)
# #     id = db.Column(db.Integer, primary_key=True)
# #     content = db.Column(db.Text, nullable=False)
# #     post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

# ##################################
# def rand_post_id():
#     rand_no=random.randint(1000,9000)
#     id=1
#     while(id):
#         rand_no=random.randint(1000,9000)
#         id=Posts.query.filter_by(id=id).first()        
#     return "pt"+str(rand_no)    
# ##################################

# @app.route('/')
# def index():    
#     posts =Posts.query.all()
#     return render_template('test.html',posts=posts)

# @app.route('/create_post', methods=['GET', 'POST'])
# def create_post():
#     if request.method == 'POST':
#         title = request.form['title']
#         content = request.form['content']
#         id=rand_post_id()
#         print(id)
#         post = Posts(id=id,title=title, content=content)
#         db.session.add(post)
#         db.session.commit()
#         posts =Posts.query.all()
#         return render_template('test.html', posts=posts)   
#         # return redirect('/')
#     return render_template('test.html', posts=posts)

# # @app.route('/reply/<int:post_id>', methods=['POST'])
# # def reply(post_id):
# #     content = request.form['content']
# #     reply = Reply(content=content, post_id=post_id)
# #     db.session.add(reply)
# #     db.session.commit()
# #     return redirect('/')

# if __name__ == "__main__":
#     app.run(debug=True, port=5500) # helps in auto refresh and find errors , port=9000, the port for the page to be shown , not 5000 to avoid duplication

