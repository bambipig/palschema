from dataclasses import dataclass


@dataclass
class AuthSchema:
    access_token: str
    expired_ts: int


@dataclass
class InfoSchema:
    pearl_id: str