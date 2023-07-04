from typing import Union ,Annotated #uvicorn main:app --reload
from fastapi import FastAPI, Query, HTTPException, Path

import vagons
#vagons.load_vagons()
app = FastAPI()
@app.get("/vagons")
def search_vagons(query: Annotated[Union[str,None], Query(max_length=8, regex="\d+")]=None):
    if query == None:
        return vagons.convert_to_json(vagons.vadons_all())
    vagon =vagons.search_vadons(query)
    if vagon == []:
        return HTTPException(status_code=404,detail=f"Not found vagon#{query}")
    return vagons.convert_to_json(vagon)

@app.get("/vagons/{vagon_number}")
def get_vagon(vagon_number:str = Path(min_length=8, max_length=8, regex="\d+")):
    vagon= vagons.search_vadons_one(vagon_number)
    if vagon == None:
        return HTTPException(status_code=404,detail=f"Not found vagon#{vagon_number}")
    return {"id:": vagon.id, "VagonNumber:": vagon.vagon_number, "VagonType:": vagon.vagon_type,  "WeightBrutto:": vagon.weight_brutto}


