from dataclasses import dataclass
from gender import Gender

@dataclass
class Person:
    name: str
    gender: Gender
