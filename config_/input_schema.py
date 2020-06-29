SHIPMENT_ID = "shipment_id"
STATUS = "status"
ENTERPRISE_ID = "enterprise_id"
TIMESTAMP = "timestamp"

_args_type = {
    SHIPMENT_ID: int,
    STATUS: str,
    ENTERPRISE_ID: int,
    TIMESTAMP: str,
}

_args_bound = {
    SHIPMENT_ID: [1,],
    STATUS: ["OutForPickup", "Delivered"],
    ENTERPRISE_ID: [1,],
    TIMESTAMP: [],
}
