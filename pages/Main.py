import streamlit as st
import time
import numpy as np
import pandas as pd

st.header('LOTTE GIANTS⚾', divider='orange')
st.title(':red[롯데의 문제점]')

id = st.text_input("학번", "")
st.session_state.id = id
name = st.text_input("이름", "")
st.session_state.name = name
score = 0
st.subheader('1. 롯데의 마지막 우승 연도는?')
que1 = st.text_input("", "")
if que1=="1992":
    score += 50

st.subheader('2. 롯데의 우승 횟수는?')
que2 = st.radio(
        "",
        options=["0", "1", "2", "3", "4"],

    )
if que2 == "2":
    score += 50
st.session_state.score = score
if st.button("제출"):
    st.switch_page("pages/result.py")
    
def stream_data(text):
    for word in text.split(" "):
        yield word + " "
        time.sleep(0.02)

if st.button("유강남"):
    Num27 = "2023년 더 이상 정보근, 지시완을 쓸 수 없다고 판단한 성민규는 박동원 대신 유강남을 4년 80억에 영입하게 된다. 아래는 2023 시즌 유강남의 성적이다"
    st.write(stream_data(Num27))
    st.write(pd.DataFrame({
        'avg': [0.264],
        'homerun': [10],
        'obp': [0.342],
        'slg': [0.384]
    }))
