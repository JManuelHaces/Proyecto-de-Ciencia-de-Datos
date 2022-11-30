import pathlib
import platform
plt = platform.system()
if plt == 'Linux': pathlib.WindowsPath = pathlib.PosixPath

import uvicorn

from fastapi import FastAPI
from fastapi import UploadFile

import warnings
from fastai.vision.all import *
from fastcore.parallel import *


warnings.filterwarnings('ignore')


from io import BytesIO
def load_image_into_numpy_array(data):
    return np.array(Image.open(BytesIO(data)))


app = FastAPI(
    title='API para generar predicciones con una red neuronal convolucional',
    description='Esta API tiene un endpoint que se'
                ' usa para obtener si un paciente presenta neumonía '
                  'en base a una radiografía de pulmón'
)


# Indicación para que se ejecute en cuanto inicie la api
@app.on_event("startup")
def load_model():
    global model_cnn  # Función para que sea global la variable
    model_cnn = load_learner('CNN_Resnet.pkl', cpu=True)


@app.get("/")
def home():
    return{"Desc": "Health Check"}


@app.post(
    path='/api/v1/classify'
)
async def create_upload_file(file: UploadFile):
    image = load_image_into_numpy_array(await file.read())
    return {"Condition": model_cnn.predict(image)[0]}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=False)