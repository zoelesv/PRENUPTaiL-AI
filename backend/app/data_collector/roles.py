from dataclasses import dataclass, field
from typing import Dict
from app.data_collector.finances import FinancialInformation


# 1.  Personal Information:
# a. Full legal names of both parties.
# b. Contact information (addresses, phone numbers, email).
# c. Date and place of the upcoming marriage.



@dataclass
class PersonalInformation:
    first_name: str = field(default_factory= lambda: "John")
    middle_name: str = field(default_factory= lambda:"")
    last_name: str = field(default=lambda: "Doe")
    addresses: Dict[str, str] = field(default_factory=dict)
    phone_numbers: Dict[str, int] = field(default_factory=dict)
    email_addresses: Dict[str, str] = field(default_factory=dict)
    marriage_date: str = field(default="04/07/1014")
    marriage_location: str = field(default="Unknown")


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
