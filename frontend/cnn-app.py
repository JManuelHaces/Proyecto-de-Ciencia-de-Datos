import streamlit as st
import requests
import json


import warnings
from fastai.vision.all import *
from fastcore.parallel import *



warnings.filterwarnings('ignore')


st.write("""
# Convolutional Neural Network App
This app predicts wether you have pneumonia or not!
""")

st.markdown('Upload your image!!')


st.subheader("Image")
image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])


if image_file is not None:

        # To See details
        file_details = {"filename":image_file.name, "filetype":image_file.type,
                        "filesize":image_file.size}  
        st.write(file_details)

        # To View Uploaded Image
        st.image(load_image(image_file),width=450)
        

        if st.button("Predict"):
            url = "http://localhost:8001/api/v1/classify" # Aquí se pone la IP del contenedor de back "IP/api/v1/classify""
            headers = {
                'Content-Type': 'application/json'
            }
            response = requests.post(url, files={"file":image_file.getbuffer()})
            prediction = json.loads(response.text)["Condition"]
            st.subheader('Prediction')
            st.write(prediction)

   


