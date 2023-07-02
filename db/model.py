from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import  declarative_base
from . import engine

Base = declarative_base()
Base.metadata.drop_all(engine)
class Vagon(Base):
    __tablename__ = "vagons"
    id = Column(Integer, primary_key=True)
    vagon_number = Column(String)
    vagon_type = Column(String)
    weight_brutto = Column(Integer)

Base.metadata.create_all(engine)



#Base.metadata.drop_all(engine)
