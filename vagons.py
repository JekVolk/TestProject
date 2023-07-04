from sqlalchemy.exc import IntegrityError, PendingRollbackError
from db import model,session
import requests
import json
def load_vagons():
    for vagon in get_vagons():
        try:
            session.add(model.Vagon(vagon_number=vagon["VagonNumber"], vagon_type=vagon["VagonType"], weight_brutto=vagon["WeightBrutto"]))
            session.commit()
        except IntegrityError:
            print('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')
        except PendingRollbackError:
            print('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')


def search_vadons(query: str):
    vagons =session.query(model.Vagon).filter(model.Vagon.vagon_number == query).all()
    return vagons

def search_vadons_one(query: str):
    vagon =session.query(model.Vagon).filter(model.Vagon.vagon_number == query).first()
    session.commit()
    return vagon

def vadons_all():
    vagons =session.query(model.Vagon).all()
    session.commit()
    return vagons

def get_vagons():
    try:
        vagons =requests.get("https://rwl.artport.pro/commercialAgent/hs/CarrWorkApp/VagonInfo").json()["Vagons"]
        return vagons
    except:
        print("erorr requests")

def convert_to_json(vagons: list):
    rezult_vagons=[]
    for vagon in vagons:
        rezult_vagons.append({"id:": vagon.id, "VagonNumber:": vagon.vagon_number, "VagonType:": vagon.vagon_type,  "WeightBrutto:": vagon.weight_brutto})
    return json.dumps(rezult_vagons)










