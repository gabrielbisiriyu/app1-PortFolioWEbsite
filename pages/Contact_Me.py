import streamlit as st 
import copy 
import send_email
st.header("Contact Me") 

def clear_field():
    st.session_state['email_field'] = "" 
    st.session_state['message_field'] = ""  


with st.form(key="form"):
    user_email=st.text_input("Your Email",key='email_field')
    user_msg=st.text_area("Your message",key='message_field')  
    button=st.form_submit_button("Submit") 
    if button:
        #print(user_msg) 
        if user_msg =="":
            st.error("message field can not be empty")
        elif "@" not in user_email:
            st.error("Incorrect Email")

        else:
            result=send_email.send_email_now(user_email,user_msg) 
            if result =="sent successfylly":          
                st.info("Message sent") 
            


