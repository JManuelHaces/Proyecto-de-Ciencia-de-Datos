
import pickle
import uvicorn
import numpy as np

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import Security, Depends, FastAPI, HTTPException
from fastapi.security.api_key import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN


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
    img: np.array


# Indicación para que se ejecute en cuanto inicie la api
@app.on_event("startup")
def load_model():
    global model_cnn  # Función para que sea global la variable
    with open(r"./model/CNN_Resnet.pkl", "rb") as f:
        model_cnn = pickle.load(f)


@app.get("/")
def home():
    return{"Desc": "Health Check"}


@app.get("/api/v1/classify")
def classify_iris(cnn: CNN):#, APIKey=Depends(get_api_key)):
    params = [cnn.img]
    pred = model_cnn.predict(params)
    dict_condition = {0: "Normal",
                 1: "With Pneumonia"}
    return {"Condition": dict_condition.get(pred[0]),
            "Desc": "Predicción hecha correctamente"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=False)