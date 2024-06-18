import streamlit as st
import pandas

st.title("The Best Company")

content = """
A good company thrives on innovation, valuing its employees and customers alike. 
It fosters a positive work environment, encourages professional growth, and maintains ethical practices. 
Commitment to quality, transparency, and social responsibility drives its success, 
ensuring lasting relationships and a strong reputation in the industry.
"""
st.write(content)

st.header("Our Team")

col1, col2, col3 = st.columns(3)

df = pandas.read_csv("data (2).csv")

with col1:
    for index, row in df[:4].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])
    
with col2:
    for index, row in df[4:8].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])
        
with col3:
    for index, row in df[8:12].iterrows():
        st.subheader(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("images (1)/" + row["image"])