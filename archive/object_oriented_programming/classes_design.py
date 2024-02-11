# https://www.youtube.com/watch?v=lX9UQp2NwTk
"""
1. Keep classes small - data focused, behaviour focused

For this example you can see Stats, Address and Person class. Person uses Stats and Address as extenstion.

2. Make classes easy to use by leveraging @properties and dunder methods

3. classes are required if we NEED to use multiple instances of them. If this is not the case modules might be better.

"""
from dataclasses import dataclass


@dataclass
class Stats:
    age: int
    height: float
    weight: float

    """
    When @property is used there is no need to use parenthesis [stats.get_bmi()] and use stats.bmi Value will be simply computed.
    There is no need to add get methods as well. Treat this function/computation to be class PROPERTY like class variable.   
    """

    @property
    def bmi(self) -> float:
        return self.weight / (self.height**2)

    """
    @staticmethods are methods not necessarily bound to class variable but logically related to class. 
    This example might be better - actually it could be as well @property
    """

    @staticmethod
    def is_adult(age: int) -> bool:
        return True if age >= 18 else False


@dataclass
class Address:
    address_line_1: str
    address_line_2: str
    city: str
    country: str

    def get_full_address(self) -> str:
        return (
            f"{self.address_line_1},{self.address_line_2}, {self.city}, {self.country}"
        )


@dataclass
class Person:
    name: str
    address: Address
    stats: Stats


def main():
    addr = Address(
        address_line_1="asdf", address_line_2="asdf 2", city="Wrocław", country="Poland"
    )

    stats = Stats(age=22, weight=120.0, height=220)

    person = Person(name="John", address=addr, stats=stats)

    # Note: bmi is @property of class stats
    print(person.stats.bmi)

    # Note: bmi is @staticmethod of class stats we can use class itself or object as interface.
    print(Stats.is_adult(18))
    print(person.stats.is_adult(stats.age))


if __name__ == "__main__":
    main()
