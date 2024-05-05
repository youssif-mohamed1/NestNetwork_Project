# import smtplib
# from email.message import EmailMessage

# def email_alert(subject, body, to):
#     msg=EmailMessage()
#     msg.set_content(body)
#     msg['subject']=subject
#     msg['to']=to
#     admin="nestnetworkhelwan@gmail.com"
#     msg['from']=admin
#     password="yntwpbzneechjelp"
#     server=smtplib.SMTP("smtp.gmail.com", 587)
#     server.starttls() # (Secure Socket Layer/Transport Layer Security), provide secure connection
#     server.login(admin, password)
#     server.send_message(msg)
    
#     server.quit()

# print("hi1")    
# email_alert("Hi", "How u doing", "youssifmo0310@gmail.com")
# print("hi2")    
