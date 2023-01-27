from dataclasses import dataclass

@dataclass
class BusinessRulesFormat:
    source: str
    destination: str


@dataclass
class BusinessRulesDataClass:
    source: str
    destination: str


@dataclass
class CustomerDataClass:
    name: str
    email: str
