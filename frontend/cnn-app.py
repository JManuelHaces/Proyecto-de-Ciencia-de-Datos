import json
import requests
import warnings
import streamlit as st
from fastai.vision.all import *
from fastcore.parallel import *

warnings.filterwarnings('ignore')


st.markdown("![Imagen_Inicio](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F4298011%2F092cd8598575c60c27fedad4d7998e66%2FjZqpV51.png?generation=1600531874588151&alt=media)")

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
            st.write("---")
            st.write("Loading Prediction...")
            loading = st.progress(0)
            # Moviendo la barra de carga hasta que termine
            for percent_complete in range(100):
                time.sleep(0.01)
                loading.progress(percent_complete + 1)
            time.sleep(1.5)
            response = requests.post(url, files={"file": image_file.getbuffer()})
            prediction = json.loads(response.text)["Condition"]
            if prediction.upper() == 'NORMAL':
                st.write(f'The patience is {prediction}')
            else:
                st.write(f'The patience has {prediction}')

   


