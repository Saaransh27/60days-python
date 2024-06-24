import streamlit as st
import pandas as pd
import os

print(os.getcwd())

# st.set_page_config(layout="wide")

# script_dir = os.path.dirname("main.py")

# # Define columns for the layout
# col1, col2 = st.columns(2)

# with col1:
#     st.image("./images/photo.png")

# with col2:
#     st.title("Saaransh Jain")
#     content = """
#     Hi, I am Saaransh! I am a Python programmer, a teacher, a college student, and ambitious to become a content creator.
#     I mainly work in Python, JavaScript, and C++ but also have experience working on Figma, Canva, Excel, and Word.
#     I completed schooling in 2022 and would complete my engineering in 2026. My goal is to get into a top IIM for an MBA.
#     """
#     st.info(content)

# content2 = """
# Below you can find some of the apps I have built in Python. Feel free to contact me!
# """
# st.info(content2)

# # Define columns for the apps section
# col3, empty_col, col4 = st.columns([1.5, 0.4, 1.5])

# # Read the data from the CSV file
# df = pd.read_csv("./data.csv", sep=";")

# # Display the first 10 rows of the dataframe in col3
# with col3:
#     for index, row in df[:10].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"])
#         st.write(f"[Source Code]({row['url']})")

# # Display the remaining rows of the dataframe in col4
# with col4:
#     for index, row in df[10:].iterrows():
#         st.header(row["title"])
#         st.write(row["description"])
#         st.image("images/" + row["image"])
#         st.write(f"[Source Code]({row['url']})")