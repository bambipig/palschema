from dataclasses import dataclass
from palschema.pearl_schema import ThingSchema, ThingWithPiecesSchema
from typing import Union
from pydantic.dataclasses import dataclass


@dataclass
class LoginRequestSchema:
    email: str
    password: str



@dataclass
class LoginResponseSchema:
    uid: str
    email: str
    master_key_encrypted: str
    private_key_encrypted: str
    access_token_encrypted: str


@dataclass
class SearchThingRequestSchema:
    type_name: str
    source_protocol: str
    source_host: str
    source_uri: str
    uri: str


@dataclass
class SearchThingResponseSchema:
    items: list[ThingSchema]
    count: int


@dataclass
class RequestThingRequestSchema:
    type_name: str
    source_protocol: str
    source_host: str
    source_uri: str


@dataclass
class RequestThingResponseSchema:
    item: Union[ThingSchema, None] = None


@dataclass
class DownloadThingRequestSchema:
    type_name: str
    source_protocol: str
    source_host: str
    source_uri: str
    uri: str


@dataclass
class DownloadThingResponseSchema:
    item: Union[ThingWithPiecesSchema, None] = None
