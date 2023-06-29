import os
import requests
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_USERNAME = os.getenv('DB_USERNAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')

connection_string = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

data = requests.get("https://rwl.artport.pro/commercialAgent/hs/CarrWorkApp/VagonInfo").json()
vagons = data["Vagons"]

Base = declarative_base()

class Vagon(Base):
    __tablename__ = DB_NAME
    id = Column(Integer, primary_key=True)
    vagon_number = Column(String)
    vagon_type = Column(String)
    weight_brutto = Column(Integer)

Base.metadata.create_all(engine)

for vagon in vagons:
    session.add(Vagon(vagon_number=vagon["VagonNumber"], vagon_type=vagon["VagonType"], weight_brutto=vagon["WeightBrutto"]))
session.commit()


vagons = session.query(Vagon).all()
for vagon in vagons:
    print(f"id: { vagon.id}")
    print(f"VagonNumber: {vagon.vagon_number}")
    print(f"VagonType: {vagon.vagon_type}")
    print(f"WeightBrutto: {vagon.weight_brutto}")
    print("---")
session.commit()


Base.metadata.drop_all(engine)

session.close()