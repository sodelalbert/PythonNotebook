# https://www.youtube.com/watch?v=0mcP8ZpUR38&t=3s

"""
inheritance - creation of multiple classes which are representing IS A relation
composition - using separate classes which have HAS relation
"""
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Optional


@dataclass
class Commission:
    """Representation of commission"""

    commission: float = 100
    contracts_landed: float = 0

    def get_payment(self) -> float:
        """Commission to be paid"""
        return self.commission * self.contracts_landed

@dataclass
class ContractCommission(Commission):
    """Represents a commission payment process based on the number of contracts landed."""

    commission: float = 100
    contracts_landed: int = 0

    def get_payment(self) -> float:
        """Returns the commission to be paid out."""
        return self.commission * self.contracts_landed

class Contract(ABC):
    @abstractmethod
    def get_payment(self) -> float:
        """Computes how much to pay employee"""


@dataclass
class Employee:
    """
    There is no direct way of creation abstract classes in Python.

    Abstract class is defined by inheritance from ABC and using @abstractmethod.
    This is done to create blueprint for children classes.

    @abstractmethod is FORCING child classes to implement it according to their needs.
    """

    name: str
    id: int
    contract: Contract
    commission: Optional[Commission] = None

    def compute_pay(self) -> float:
        """Compute how much employee should be paid."""
        payout = self.contract.get_payment()
        if self.commission is not None:
            payout += self.commission.get_payment()
        return payout
@dataclass
class HourlyContract(Contract):
    """Contract type for an employee being paid on an hourly basis."""

    pay_rate: float
    hours_worked: int = 0
    employer_cost: float = 1000

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked + self.employer_cost


@dataclass
class SalariedContract(Contract):
    """Contract type for an employee being paid a monthly salary."""

    monthly_salary: float
    percentage: float = 1

    def get_payment(self) -> float:
        return self.monthly_salary * self.percentage


@dataclass
class FreelancerContract(Contract):
    """Contract type for a freelancer (paid on an hourly basis)."""

    pay_rate: float
    hours_worked: int = 0
    vat_number: str = ""

    def get_payment(self) -> float:
        return self.pay_rate * self.hours_worked


def main() -> None:
    """Main function."""

    henry_contract = HourlyContract(pay_rate=50, hours_worked=100)
    henry = Employee(name="Henry", id=12346, contract=henry_contract)
    print(
        f"{henry.name} worked for {henry_contract.hours_worked} hours "
        f"and earned ${henry.compute_pay()}."
    )

    sarah_contract = SalariedContract(monthly_salary=5000)
    sarah_commission = ContractCommission(contracts_landed=10)
    sarah = Employee(
        name="Sarah", id=47832, contract=sarah_contract, commission=sarah_commission
    )
    print(
        f"{sarah.name} landed {sarah_commission.contracts_landed} contracts "
        f"and earned ${sarah.compute_pay()}."
    )


if __name__ == "__main__":
    main()