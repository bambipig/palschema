from dataclasses import dataclass
from typing import Dict


@dataclass
class LoginRequestSchema:
    email: str


@dataclass
class LoginResponseSchema:
    uid: str
    email: str
    master_key_encrypted: str
    public_key: str
    private_key_encrypted: str
    access_token_encrypted: str
    fernet_key_encrypted: str


@dataclass
class ListResponseSchema:
    items: list
    count: int


@dataclass
class ThingSchema:
    type_name: str
    source_uri: str
    thing_uuid: str
    uri: str
    status: str
    meta_id: str = None
    uuid: str = None
    source_host: str = None


@dataclass
class SearchThingRequestSchema:
    keywords: list[str]

    type_name: str = None
    source_host: str = None


@dataclass
class SearchThingResponseSchema(ListResponseSchema):
    items: list[ThingSchema]

    def __post_init__(self):
        self.items = [ThingSchema(**_e) for _e in self.items]


@dataclass
class RequestThingSourceMetaSchema:
    type_name: str
    source_host: str
    source_uri: str


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
class ResourceSchema:
    uuid: str
    size: int
    sha256_hash: str
    url: str


@dataclass
class DownloadThingResponseSchema:
    thing_uuid: str
    type_name: str
    source_host: str
    source_uri: str
    uri: str
    resources: Dict
