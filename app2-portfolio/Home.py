import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    pass

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
st.info(content2)

col3, empty_col, col4 = st.columns([1.5, 0.4, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")