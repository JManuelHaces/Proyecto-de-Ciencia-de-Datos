import uvicorn
import numpy.typing as npt

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN

import warnings
from fastai.vision.all import *
from fastcore.parallel import *
import pickle


warnings.filterwarnings('ignore')


API_KEY = "1234567asdfgh"
API_KEY_NAME = "access_token"

api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=False)


app = FastAPI(
    title='API para generar predicciones con una red neuronal convolucional',
    description='Esta API tiene un endpoint que se'
                ' usa para obtener si un paciente presenta neumonía '
                  'en base a una radiografía de pulmón'
)



def get_api_key(api_key_query: str = Security(api_key_query)):
    if api_key_query == API_KEY:
        return api_key_query
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN,
            detail="Could not validate credentials")


class CNN(BaseModel):
    img = np.ndarray


# Indicación para que se ejecute en cuanto inicie la api
@app.on_event("startup")
def load_model():
    global model_cnn  # Función para que sea global la variable
    model_cnn = load_learner('.\model\CNN_Resnet.pkl', cpu=True)


@app.get("/")
def home():
    return{"Desc": "Health Check"}


@app.get("/api/v1/classify")
def classify_condition(cnn: CNN):#, APIKey=Depends(get_api_key)):
    pred = model_cnn.predict(cnn['img'])[0]
    return {"Condition": pred,
            "Desc": "Successfully predicted"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=False)