"""
Dataclasses

Type of classes which are data oriented.

- no need to create constructor __init__ which will be generated automatically.
- no need to create __str__ to represent dataclass fields. Useful when there is big number of class fields.
- default values can be initialized
    - filed method can be used to create individual instance of variable
    - individual ID can be generated by passing function to default factory
    - adding init=false is removing that field from __init__ method which is not allowing users to modify it during
      initialization of a class
- in order to construct more variables based on class variables __post_init__ dunder method can be used. this is
  useful if we would like to add distinct identifiers per our class instance based on arguments passed in init.
   - To indicate that value is private _ (underscore to be added) - not supposed to be changed outside class
   - To exclude printing internal information about class information (applicable for _) you can exclude it from __repr_ in field function.
- to make constant variable from dataclass add frozen=True to decorator. By the default it's possible to change value of dataclass.

References:
    - https://www.youtube.com/watch?v=CvQ7e6yUtnw
    - https://docs.python.org/3/library/dataclasses.html

"""
import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name  # Instance variable
        self.address = address

    def __str__(self) -> str:
        return f"{self.name}, {self.address}"


@dataclass(frozen=True)
class ConstantVariables:
    PI: float = 3.14
    E: float = 2.73


@dataclass
class Persona:
    name: str  # Class variable
    address: str
    active: bool = True
    email_addresses: list[str] = field(default_factory=list)
    id: str = field(init=False, default_factory=generate_id)
    const: float = ConstantVariables.PI
    _search_string: str = field(init=False)

    def __post_init__(self) -> None:
        self._search_string = f"{self.name} {self.address}"


def main() -> None:
    # person = Person(name="John", address="Monument Valley 123")
    # print(person)

    persona = Persona(name="John", address="Monument Valley 123")
    print("Persona id value", persona.id)

    print(f"Constant variables from dataclass {ConstantVariables.PI}")

    print(persona)


if __name__ == "__main__":
    main()
