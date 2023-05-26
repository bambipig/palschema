from dataclasses import dataclass
from dataclasses import  field
from typing import List
from pydantic import BaseModel as BaseSchema

@dataclass
class InfoSchema:
    pearl_id: str


@dataclass
class PearlSchema:
    host: str
    port: int


@dataclass
class ThingPieceSchema:
    bytes_size: int
    sha256_hash: str
    piece_idx: int
    dialect: str
    storage_uri: str


@dataclass
class ThingSchema:
    thing_uuid: str
    # ttype_uuid: str
    # source_uuid: str
    # source_uri: str
    # uri: str
    #
    # pieces: List[ThingPieceSchema] = field(default_factory=list)


class TaskSchema(BaseSchema):
    """Task Schema"""
    task_uuid: str



ThingWithPiecesSchema = ThingSchema
