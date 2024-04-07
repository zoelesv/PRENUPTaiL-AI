from dataclasses import dataclass, field
from typing import Dict, Optional
from backend.app.data_collector.finances import FinancialInformation


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
    religion_affiliation: Optional[str] = None
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
            marriage_location=None,
            religion_affiliation=None
        )
         
         self.person1.finances = FinancialInformation(
             tangible_assets=None, 
             nontangible_assets=None, 
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
            marriage_location=None,
            religion_affiliation=None
        )
         
         self.person2.finances = FinancialInformation(
             tangible_assets=None, 
             nontangible_assets=None,  
             debts=None,
             income_sources=None,
             financial_obligations=None)
        


