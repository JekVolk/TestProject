from typing import Union  #uvicorn main:app --reload
from fastapi import FastAPI
import vagons
#vagons.load_vagons()
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello world app"}
@app.get("/vagons")
def search_vadonser(vagon_number : str):
    vagons_dictonari=vagons.search_vadons(vagon_number)
    return vagons_dictonari if "0" in vagons_dictonari else vagons.vadons_all()

@app.get("/vagons/{vagon_number}")
def search_vadons(vagon_number: str):
    vagons_dictonari=vagons.search_vadons(vagon_number)
    return vagons_dictonari if "0" in vagons_dictonari else {"erorr":"404 не знайдено в базі даних"}


