from typing import Union ,Annotated #uvicorn main:app --reload
from fastapi import FastAPI, Query, HTTPException, Path

import vagons_service
#vagons.load_vagons()
app = FastAPI()
@app.get("/vagons")
def search_vagons(query: Annotated[Union[str,None], Query(max_length=8, regex="\d+")]=None):
    if query == None:
        return vagons_service.vagons_all()
    vagons= vagons_service.search_vagons(query)
    return vagons

@app.get("/vagons/{vagon_number}")
def get_vagon(vagon_number:str = Path(regex="^\d{8}$")):
    vagon= vagons_service.search_vagon_one(vagon_number)
    if vagon == None:
        return HTTPException(status_code=404,detail=f"Not found vagon#{vagon_number}")
    return vagon



