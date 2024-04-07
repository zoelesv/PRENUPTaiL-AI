from dataclasses import dataclass
from typing import Dict, Optional



# 3. Desired Distribution of Assets and Debts:
# a. How do both parties want to divide their assets in case of divorce or separation? For example, who keeps which properties, investments, or businesses?
# b. How do both parties want to handle debts acquired during the marriage? Who will be responsible for which debts?
# c. Are there specific assets or properties that either party wishes to keep separate or retain full ownership of?

# 4. Spousal Support (Alimony):
# a. Do the parties wish to address spousal support (alimony) in the event of divorce or separation? If so, what are their expectations regarding the amount and duration of support?

# 5. Estate Planning and Inheritance:
# a. Are there specific assets that either party wishes to designate as separate property for inheritance purposes?
# b. Do both parties have existing estate plans (wills, trusts) that need to be considered in the prenuptial agreement?


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