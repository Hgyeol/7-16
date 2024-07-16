import streamlit as st

if 'key' in st.session_state:
    st.write(st.session_state.key)