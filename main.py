from typing import Union, Annotated #uvicorn main:app --reload
from fastapi import FastAPI, Query, HTTPException, Path
from vagons_pakage import models_pydantic, vagons_service
#vagons_service.load_vagons()

app = FastAPI()
@app.get("/vagons_pakage")
def search_vagons(query: Annotated[Union[str,None], Query(max_length=8, regex="\d+")]=None):
    if query == None:
        return vagons_service.vagons_all()
    vagons= vagons_service.search_vagons(query)
    return vagons

@app.get("/vagons_pakage/{vagon_number}")
def get_vagon(vagon_number:str = Path(regex="^\d{8}$")):
    vagon= vagons_service.search_vagon_one(vagon_number)
    if vagon == None:
        return HTTPException(status_code=404,detail=f"Not found vagon#{vagon_number}")
    return vagon

@app.post("/vagons_pakage")
def post_vagon(vagon: models_pydantic.UniversalVagon):
    return vagons_service.add_vagon(vagon)git push

@app.put("/vagons_pakage/{vagon_number}")
def put_vagon(vagon: models_pydantic.UniversalVagon):
    return vagons_service.put_vagon(vagon)

@app.patch("/vagons_pakage/{vagon_number}")
def patch_vagon(vagon: models_pydantic.EditedVagon):
    return vagons_service.edit_vagon(vagon)

@app.delete("/vagons_pakage/{vagon_number}")
def delete_vagon(vagon_number:str = Path(regex="^\d{8}$")):
    return vagons_service.delete_vagon(vagon_number)