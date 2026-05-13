from dataclasses import dataclass

@dataclass
class User:
    full_name: str
    email: str
    password: str
    phone: str