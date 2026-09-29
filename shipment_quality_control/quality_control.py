'''Mock Coding #1 — Shipment Quality Control
Trabajas en un sistema que controla envíos procedentes de distintas fábricas.
Disponemos de un histórico de componentes que anteriormente han dado problemas de calidad
en cada fábrica.
Tenemos estas estructuras:
'''
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class DefectRecord:
    factory_id: str
    component_code: str


@dataclass
class Component:
    code: str
    quantity: int


@dataclass
class Shipment:
    shipment_id: str
    factory_id: str
    components: list[Component]

defect_records = [
    DefectRecord(factory_id="factory-1", component_code="CPU-10"),
    DefectRecord(factory_id="factory-1", component_code="BAT-20"),
    DefectRecord(factory_id="factory-2", component_code="SCR-30"),
]

# New shipment to be checked
shipments = [
    Shipment(
        shipment_id="shipment-1",
        factory_id="factory-1",
        components=[
            Component(code="CPU-10", quantity=2),
            Component(code="RAM-40", quantity=5),
        ],
    ),
    Shipment(
        shipment_id="shipment-2",
        factory_id="factory-1",
        components=[
            Component(code="SCR-30", quantity=1),
            Component(code="RAM-40", quantity=2),
        ],
    ),
    Shipment(
        shipment_id="shipment-3",
        factory_id="factory-2",
        components=[
            Component(code="SCR-30", quantity=3),
        ],
    ),
]

# Implement
'''
Un shipment requiere inspección si contiene al menos un componente que previamente
haya tenido un defecto en esa misma fábrica.
Con los datos anteriores, esperamos:

[    "shipment-1",    "shipment-3",]

Fíjate en shipment-2: contiene SCR-30, que aparece en el histórico, pero ese defecto
corresponde a "factory-2" y el shipment viene de "factory-1". Por tanto, no debe marcarse.
'''
def find_shipments_requiring_inspection(
    defect_records: list[DefectRecord],
    shipments: list[Shipment],
) -> list[str]:
    shipments_requiring_inspection: list[str] = []
    defects_by_factory: dict[str, set[str]] = defaultdict(set)

    for defect_record in defect_records:
        defects_by_factory[defect_record.factory_id].add(defect_record.component_code)

    for shipment in shipments:
        defective_components = defects_by_factory.get(shipment.factory_id)
        if not defective_components:
            continue

        for shipment_component in shipment.components:
            if shipment_component.code in defective_components:
                shipments_requiring_inspection.append(shipment.shipment_id)
                break

    return shipments_requiring_inspection