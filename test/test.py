import pytest
from app.vagons_pakage import vagons_service,models_pydantic

@pytest.mark.parametrize(
    "number_vagon, type_vagon, brutto_vagon, rezult",
    [
        ("12345678", "РТР", 4544512, {"VagonNumber:": "12345678", "VagonType:": "РТР", "WeightBrutto:": 4544512}),
        ("12345678", "РТР", 4544512, 'duplicate key value violates uniqueness constraint "wagons_wagon_number_key"'),
        ("12345678", "ФФФ", 11254, 'duplicate key value violates uniqueness constraint "wagons_wagon_number_key"'),
        #("00000000", "РТР", 4544512, {"VagonNumber:": "00000000", "VagonType:": "РТР", "WeightBrutto:": 4544512}),
    ]
)
def test_add(number_vagon, type_vagon, brutto_vagon, rezult):
    vagon = models_pydantic.UniversalVagon(vagon_number = number_vagon,vagon_type = type_vagon,weight_brutto = brutto_vagon)
    assert vagons_service.add_vagon(vagon) == rezult
