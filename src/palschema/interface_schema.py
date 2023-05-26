from dataclasses import dataclass
from palschema.pearl_schema import ThingSchema, ThingWithPiecesSchema
from typing import Union


@dataclass
class LoginRequestSchema:
    email: str



@dataclass
class LoginResponseSchema:
    uid: str
    email: str
    master_key_encrypted: str
    private_key_encrypted: str
    access_token_encrypted: str
    fernet_key_encrypted: str


@dataclass
class ListResponseSchema:
    items: list
    count: int


@dataclass
class SearchThingRequestSchema:
    keywords: list[str]

    type_name: str = None
    source_host: str = None


@dataclass
class SearchThingResponseSchema(ListResponseSchema):
    items: list[ThingSchema]


@dataclass
class RequestThingRequestSchema:
    type_name: str
    source_protocol: str
    source_host: str
    source_uri: str


@dataclass
class RequestThingResponseSchema:
    thing_uuid: str
    task_uuid: str


@dataclass
class DownloadThingRequestSchema:
    thing_uuid: str


@dataclass
class DownloadThingResponseSchema:
    thing_uuid: str
    type_name: str
    source_host: str
    source_uri: str
    uri: str
    resources: dict
