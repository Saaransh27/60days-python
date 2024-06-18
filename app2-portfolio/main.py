import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photos.png.jpg", width = 500)

with col2:
    st.title("Saaransh Jain")
    content = """
    Hi, I am Saaransh! I am a python programmer, a teacher, a college student and ambitious to become a content creator.
    I mainly work in Python, javascript and C++ but also have experience in working on Figma, Canva, Excel and Word.
    I completed schooling in 2022 and would complete my engineering in 2026. My goal is to get in top IIM,
    for MBA.
    """
    
    st.info(content)

content2 = """
Below you can find some of the apps i have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, col4 = st.columns(2)

with col3:
    