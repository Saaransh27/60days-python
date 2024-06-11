import streamlit as st
from PIL import Image

uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    img = Image.open(uploaded_image)
    grey_photo = img.convert("L")
    st.image(grey_photo)

with st.expander("start camera"):
    #Start the camera
    camera_image = st.camera_input("Camera")

if camera_image:
    #create a pillow image instance
    img = Image.open(camera_image)
    
    #convert pillow image to grey scale
    gray_img = img.convert("L")
    
    #show grey scale as output on webpage
    st.image(gray_img)
    
