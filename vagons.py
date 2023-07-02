from db import model ,session
import request

def load_vagons():
    for vagon in request.vagons:
        session.add(model.Vagon(vagon_number=vagon["VagonNumber"], vagon_type=vagon["VagonType"],weight_brutto=vagon["WeightBrutto"]))
    session.commit()

def search_vadons(query: str):
    vagons_list =session.query(model.Vagon).filter(model.Vagon.vagon_number == query).all()
    session.commit()
    vagons_dictonari={}
    list_nomer=0
    for vagon in vagons_list:
        vagons_dictonari[str(list_nomer)]={"id:": vagon.id, "VagonNumber:": vagon.vagon_number, "VagonType:": vagon.vagon_type,  "WeightBrutto:": vagon.weight_brutto}
        list_nomer+=1
    return vagons_dictonari

def vadons_all():
    vagons_list =session.query(model.Vagon).all()
    session.commit()
    vagons_dictonari={}
    list_nomer=0
    for vagon in vagons_list:
        vagons_dictonari[str(list_nomer)]={"id:": vagon.id, "VagonNumber:": vagon.vagon_number, "VagonType:": vagon.vagon_type,  "WeightBrutto:": vagon.weight_brutto}
        list_nomer+=1
    return vagons_dictonari





