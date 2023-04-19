from dataclasses import dataclass


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
    pass


@dataclass
class SearchThingResponseSchema:
    pass


@dataclass
class RequestThingRequestSchema:
    pass


@dataclass
class RequestThingResponseSchema:
    pass


@dataclass
class DownloadThingRequestSchema:
    pass


@dataclass
class DownloadThingResponseSchema:
    pass