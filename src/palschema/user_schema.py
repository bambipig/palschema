from dataclasses import dataclass


@dataclass
class LoginSchema:
    email: str


@dataclass
class AuthSchema:
    access_token: str
    expired_ts: int


