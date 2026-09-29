from shipment_quality_control.quality_control import (
    Component,
    DefectRecord,
    Shipment,
    defect_records,
    find_shipments_requiring_inspection,
    shipments,
)


def test_shipments_requiring_inspection():
    expected_shipments = ["shipment-1", "shipment-3"]
    result = find_shipments_requiring_inspection(defect_records, shipments)
    assert result == expected_shipments

def test_no_shipments():
    assert find_shipments_requiring_inspection(
        [DefectRecord("factory-1", "CPU-10")],
        [],
    ) == []

def test_shipment_without_components():
    assert find_shipments_requiring_inspection(
        [DefectRecord("factory-1", "CPU-10")],
        [Shipment("shipment-1", "factory-1", [])],
    ) == []

def test_same_component_wrong_factory():
    assert find_shipments_requiring_inspection(
        [DefectRecord("factory-2", "CPU-10")],
        [
            Shipment(
                "shipment-1",
                "factory-1",
                [Component("CPU-10", 1)],
            )
        ],
    ) == []
