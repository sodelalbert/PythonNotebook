# https://www.youtube.com/watch?v=0mcP8ZpUR38&t=3s

"""
inheritance - creation of multiple classes which are representing IS A relation

Problems with variants of objects leading to code duplication.
Strong coupling using super() method

composition - using separate classes which have HAS relation
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Employee(ABC):
    """
    There is no direct way of creation abstract classes in Python.

    Abstract class is defined by inheritance from ABC and using @abstractmethod.
    This is done to create blueprint for children classes.

    @abstractmethod is FORCING child classes to implement it according to their needs.
    """

    name: str
    id: int

    @abstractmethod
    def compute_pay(self) -> float:
        """Compute how much employee should be paid."""


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    commission: float = 100
    contracts_landed: float = 0
    pay_rate: float = 0
    hours_worked: int = 0
    employer_cost: float = 1000

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return (
            self.pay_rate * self.hours_worked
            + self.employer_cost
            + self.commission * self.contracts_landed
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 0
    percentage: float = 1

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.monthly_salary * self.percentage


@dataclass
class SalariedEmployeeWithCommission(SalariedEmployee):
    """Employee that's paid based on a fixed monthly salary and gets commission"""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed


@dataclass
class Freelancer(Employee):
    """Freelancer that's paid based on number of worked hours."""

    pay_rate: float = 0
    hours_worked: int = 0
    vat_number: str = ""

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return self.pay_rate * self.hours_worked


@dataclass
class FreelancerWithCommission(Freelancer):
    """Freelancer that's paid based on number of worked hours."""

    commission: float = 100
    contracts_landed: float = 0

    def compute_pay(self) -> float:
        """Compute how much the employee should be paid."""
        return super().compute_pay() + self.commission * self.contracts_landed


def main() -> None:
    """Main function."""

    henry = HourlyEmployee(name="Henry", id=12346, pay_rate=50, hours_worked=100)
    print(
        f"{henry.name} worked for {henry.hours_worked} hours and earned ${henry.compute_pay()}."
    )

    sarah = SalariedEmployeeWithCommission(
        name="Sarah", id=47832, monthly_salary=5000, contracts_landed=10
    )
    print(
        f"{sarah.name} landed {sarah.contracts_landed} contracts and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()
