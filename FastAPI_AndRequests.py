from typing import Union  #uvicorn FastAPI_AndRequests:app --reload
import requests
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world app"}

@app.get("/vagons")
def read_vagon():
    response = requests.get("https://rwl.artport.pro/commercialAgent/hs/CarrWorkApp/VagonInfo")
    return {"Vagon": response.json()}
