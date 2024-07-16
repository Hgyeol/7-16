import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('secret.json')

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://test-b40b6-default-rtdb.firebaseio.com/'
    })

gId = db.reference('id').get()
gPassword = db.reference('password').get()
st.write(type(gId))
st.title("로그인")

id = st.text_input("아이디", "")
password = st.text_input("비밀번호", "")

if st.button("로그인"):
    if id == gId & password == gPassword:
        st.switch_page("pages/Main.py")