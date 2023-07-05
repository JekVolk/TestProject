from sqlalchemy.exc import IntegrityError, PendingRollbackError
from sqlalchemy.orm.exc import UnmappedInstanceError
from db import model,session
import requests

def load_vagons():
    for vagon in get_vagons():
        try:
            session.add(model.Vagon(vagon_number=vagon["VagonNumber"], vagon_type=vagon["VagonType"], weight_brutto=vagon["WeightBrutto"]))
            session.commit()
        except IntegrityError:
            print('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')
        except PendingRollbackError:
            print('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')


def search_vagons(query: str):
    vagons =session.query(model.Vagon).filter(model.Vagon.vagon_number == query).all()
    return format_vagons(vagons)

def search_vagon_one(query: str):
    vagon =session.query(model.Vagon).filter(model.Vagon.vagon_number == query).first()
    return format_vagon(vagon)

def vagons_all():
    vagons =session.query(model.Vagon).all()
    return format_vagons(vagons)

def get_vagons():
    try:
        vagons =requests.get("https://rwl.artport.pro/commercialAgent/hs/CarrWorkApp/VagonInfo").json()["Vagons"]
        return vagons
    except:
        print("erorr requests")

def format_vagon(vagon: model.Vagon):
    if vagon== None:
        return None
    return {
        "VagonNumber:": vagon.vagon_number,
        "VagonType:": vagon.vagon_type,
        "WeightBrutto:": vagon.weight_brutto}

def format_vagons(vagons: list):
    convertyed_vagons = map(format_vagon,vagons)
    return list(convertyed_vagons)

def post_vagons(vagon):
    try:
        session.add(model.Vagon(vagon_number=vagon.vagon_number, vagon_type=vagon.vagon_type, weight_brutto=vagon.weight_brutto))
        session.commit()
        return search_vagon_one(vagon.vagon_number)
    except IntegrityError:
        return ('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')
    except PendingRollbackError:
        return ('duplicate key value violates uniqueness constraint "wagons_wagon_number_key"')

def patch_vagons(edited_vagon):
    vagon_old = session.query(model.Vagon).filter(model.Vagon.vagon_number == edited_vagon.vagon_number).first()
    if edited_vagon.vagon_type != None :   #and edited_vagon.vagon_type== vagon_old.vagon_type
        vagon_old.vagon_type=edited_vagon.vagon_type                         #AttributeError: 'NoneType' object has no attribute 'vagon_type'
    if edited_vagon.vagon_type != None :  # and edited_vagon.vagon_type== vagon_old.vagon_type
        vagon_old.weight_brutto=edited_vagon.weight_brutto
    session.commit()
    return search_vagon_one(edited_vagon.vagon_number)

def delete_vagons(vagon_number: str):
    try:
        session.delete(session.query(model.Vagon).filter(model.Vagon.vagon_number == vagon_number).first())
        session.commit()
        return "Операція виконана успішно"
    except UnmappedInstanceError:
        return "такий вагон не знайден в базі даних"










