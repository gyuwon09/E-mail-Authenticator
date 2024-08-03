import smtplib
from email.message import EmailMessage
import os
import random

#change to your service name
service_name = "default"

def email_authenticator(in1):
    input_1 = in1     #target
    random_num = random.randint(1000,9999)

    #change email message to what you need
    email_message = f"""

[E-mail Authenticator System]

This is E-mail Authenticator System
Please input this code on your service.
: {random_num}


Thank you :)
"""

    smtp_server = os.getenv("smtp_server") #smtp server setting
    smtp_port = os.getenv("smtp_port") #smtp port setting
    sender_email = os.getenv("sender")  #sender email setting
    sender_password = os.getenv("email_password")  #sender email password setting

    email = EmailMessage()
    email.set_content(email_message) 
    email["Subject"] = (f"E-mail Authenticator")
    email["From"] = service_name
    email["To"] = input_1
    
    try: #email send
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # TLS setting
            server.login(sender_email, sender_password)  #email login
            server.send_message(email)  #send email
        return random_num
    except Exception as e:
        print(f"Error : {e}")
        return False
