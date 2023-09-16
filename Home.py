import streamlit as st 
import PIL as pl  
import csv 
import pandas as pd
st.set_page_config(page_title="Home",initial_sidebar_state="auto")
col1,col2=st.columns(2)
with col1:
    st.image("images/pic.jpg")  
with col2:
    st.title("Gabriel Bisiriyu") 
    content='''
    Hi, i am Gabriel Bisiriyu. I am a python programmer,designer and a seasoned utility tester.
    I am a Computer Engineering student of the University Of Lagos in Nigeria     
        '''
    st.info(content)    

content='''
Below you can find some of the apps i have built with Python. Feel free to contact me.
'''
st.write(content) 

df=pd.read_csv("data.csv",sep=';')
col3,col4,col5=st.columns(3) 
num=len(df)
num=int(num*0.5+1) 
with col3:
    for index,data in df[:num].iterrows():
         st.title(data["title"])
         st.write(data["description"]) 
         st.image(data["image"])
         st.markdown("[view source code](%s)"%data["url"])   
         st.write('-'*34)

with col4:
    st.write("   ") 

with col5:
    for index,data in df[num:].iterrows():
         st.title(data["title"])
         st.write(data["description"]) 
         st.image(data["image"])
         st.markdown("[view source code](%s)"%data["url"])   
         st.write('-'*34)

