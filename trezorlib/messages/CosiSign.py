# Automatically generated by pb2py
from .. import protobuf as p


class CosiSign(p.MessageType):
    FIELDS = {
        1: ('address_n', p.UVarintType, p.FLAG_REPEATED),
        2: ('data', p.BytesType, 0),
        3: ('global_commitment', p.BytesType, 0),
        4: ('global_pubkey', p.BytesType, 0),
    }
    MESSAGE_WIRE_TYPE = 73
