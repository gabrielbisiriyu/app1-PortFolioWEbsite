import streamlit as st 
import send_email
st.header("Contact Me") 

with st.form(key="form"):
    user_email=st.text_input("Your Email")
    user_msg=st.text_area("Your message") 
    button=st.form_submit_button("Submit") 
    if button:
        #print(user_email) 
        #print(user_msg) 
        if user_msg =="":
            #result=="message field can not be empty"
            #print("message field can not be empty")
            st.error("message field can not be empty")
        elif "@" not in user_email:
            st.error("Incorrect Email")

        else:
            result=send_email.send_email_now(user_email,user_msg) 
            if result =="sent successfylly": 
                st.info("Message sent") 
            #else:
            #    st.error("Message not sent")  
            #elif result=="Incorrect Email":
            #    st.error("Incorrect Email")
            

