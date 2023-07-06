from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base
from . import engine

Base = declarative_base()
class Vagon(Base):
    __tablename__ = "vagons_pakage"
    id = Column(Integer, primary_key=True)
    vagon_number = Column(String, unique=True)
    vagon_type = Column(String)
    weight_brutto = Column(Integer)

Base.metadata.create_all(engine)



#Base.metadata.drop_all(engine)
