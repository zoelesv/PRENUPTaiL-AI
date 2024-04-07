from dataclasses import dataclass, field
from typing import Dict, Optional
from app.data_collector.finances import FinancialInformation


# 1.  Personal Information:
# a. Full legal names of both parties.
# b. Contact information (addresses, phone numbers, email).
# c. Date and place of the upcoming marriage.


@dataclass
class PersonalInformation:
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    addresses: Dict[str, str]
    phone_numbers: Dict[str, str]
    email_addresses: Dict[str, str]
    marriage_date: str
    marriage_location: str
    legal_representation_reviewed: bool = field(default=False)


@dataclass
class Person:
    personal_information: PersonalInformation
    finances: FinancialInformation


###

@dataclass
class AllPersons:
    person1: Person
    person2: Person

    def __post_init__(self):

         self.person1.personal_information = Person(
            first_name=None,
            middle_name=None,
            last_name=None,
            addresses={"home": None},
            phone_numbers={"home": None, "cell": None},
            email_addresses={"home": None},
            marriage_date=None,
            marriage_location=None
        )
         
         self.person1.finances = FinancialInformation(
             assets=None, 
             debts=None,
             income_sources=None,
             financial_obligations=None)


         ###
         
         self.person2.personal_information = Person(
            first_name=None,
            middle_name=None,
            last_name=None,
            addresses={"home": None},
            phone_numbers={"home": None, "cell": None},
            email_addresses={"home": None},
            marriage_date=None,
            marriage_location=None
        )
         
         self.person2.finances = FinancialInformation(
             assets=None, 
             debts=None,
             income_sources=None,
             financial_obligations=None)
         


@dataclass
class DistributionAgreement:
    asset_division: Dict[str, str]
    debt_responsibility: Dict[str, str] 
    legal_representation_reviewed: bool

    def assign_asset(self, asset_name: str, owner_name: str):
        self.asset_division[asset_name] = owner_name

    def assign_debt_responsibility(self, debt_name: str, responsible_party: str):
        self.debt_responsibility[debt_name] = responsible_party

    def legal_representation_review(self):
        self.legal_representation_reviewed = True


@dataclass
class SpousalSupport:
    has_agreement: bool
    amount: Optional[float] = None
    duration: Optional[int] = None  # Duration in months
    legal_representation_reviewed: bool

    def set_spousal_support(self, amount: float, duration: int):
        self.has_agreement = True
        self.amount = amount
        self.duration = duration

    def legal_representation_review(self):
        self.legal_representation_reviewed = True


@dataclass
class EstatePlanning:
    separate_property: Dict[str, str]
    existing_plans: Optional[str] = None
    legal_representation_reviewed: bool

    def designate_separate_property(self, property_name: str, owner_name: str):
        self.separate_property[property_name] = owner_name
    
    def legal_representation_review(self):
        self.legal_representation_reviewed = True


@dataclass
class PrenupAgreement:
    personal_info: AllPersons
    distribution_agreement: DistributionAgreement
    spousal_support: SpousalSupport
    estate_planning: EstatePlanning
    legal_representation_reviewed: bool

    
    def legal_representation_review(self):
        self.legal_representation_reviewed = True

