from pydantic import BaseModel , Field

class UniversalVagon(BaseModel):
    vagon_number: str = Field(regex="^\d{8}$")
    vagon_type: str = Field(min_length=3,max_length=3,regex="[А-ЩЬЮЯЇІЄҐ]")   #^[А-ЩЬЮЯЇІЄҐ]{3}$
    weight_brutto : int =Field(ge=0)

class EditedVagon(BaseModel):
    vagon_number: str = Field(regex="^\d{8}$")
    vagon_type: str = Field(min_length=3,max_length=3,regex="[А-ЩЬЮЯЇІЄҐ]",default=None, optional=True)   #^[А-ЩЬЮЯЇІЄҐ]{3}$
    weight_brutto: int = Field(ge=0,default=None, optional=True)
