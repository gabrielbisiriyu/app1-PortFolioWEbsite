import smtplib # THIS IS AN EMAIL LIBRARY  
import ssl 
import streamlit as st
import os
def send_email_now(email,form_filler_message):
    standar_host = "smtp.gmail.com"   # THIS IS A STANDARD HOST FOR Gmail  
    standard_port = 465  # ALSO STANDARD PORT 
    username="guyex1996@gmail.com"
    
    password=os.getenv("PASSWORD") 
    print(password)
    receiver="guyex1996@gmail.com" 

    subject="Subject: JOB NOTIFICATION"+" \n"
     
    form_filler_message=subject+form_filler_message +'\n'+ email 
    my_context=ssl.create_default_context() # FOR SENDING SECURE EMAIL  

    with smtplib.SMTP_SSL(host=standar_host,port=standard_port,context=my_context) as server:
        server.login(username,password) 
        try:
            server.sendmail(username,receiver,form_filler_message)  
            if form_filler_message=="":
                pass
                #return "message field can not be empty" 
            
            elif "@" not in email: 
                pass
                #return "Incorrect Email"

            else: 
                return "sent successfylly"  
        except:
            pass

#send_email_now("azeeztoluwalope12@gmail.com","try again") 
