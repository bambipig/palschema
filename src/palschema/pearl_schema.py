from dataclasses import dataclass
from dataclasses import  field
from typing import List


@dataclass
class InfoSchema:
    pearl_id: str


@dataclass
class ThingPieceSchema:
    bytes_size: int
    sha256_hash: str
    piece_idx: int
    dialect: str
    storage_uri: str


@dataclass
class ThingSchema:
    ttype_uuid: str
    source_uuid: str
    source_uri: str
    thing_uuid: str
    uri: str

    pieces: List[ThingPieceSchema] = field(default_factory=list)

