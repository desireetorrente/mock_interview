from .quality_control import (
    defect_records,
    find_shipments_requiring_inspection,
    shipments,
)

if __name__ == "__main__":
    find_shipments_requiring_inspection(defect_records, shipments)
