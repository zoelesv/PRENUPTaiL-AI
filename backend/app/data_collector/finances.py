from dataclasses import dataclass, field
from typing import Dict

from app.data_collector.person import Person

# 2. Financial Information:
# a. List of individual assets owned by each party (e.g., real estate, vehicles, investments, business interests).
# b. List of individual debts owed by each party (e.g., mortgages, loans, credit card debts).
# c. Income sources and approximate annual income for each party.
# d. Any existing financial agreements or obligations (e.g., alimony, child support from previous relationships).


@dataclass
class FinancialInformation:
    tangible_assets: Dict[str, float] = field(default_factory=dict)
    nontangible_assets: Dict[str, float] = field(default_factory=dict)
    debts: Dict[str, float] = field(default_factory=dict)
    income_sources: Dict[str, float] = field(default_factory=dict)
    financial_obligations: Dict[str, float] = field(default_factory=dict)

    def add_tangible_asset(self, name: str, value: float):
        self.tangible_assets[name] = value
    
    def add_nontangible_asset(self, name: str, value: float):
        self.nontangible_assets[name] = value

    def add_debt(self, name: str, amount: float):
        self.debts[name] = amount

    def total_assets(self) -> float:
        return sum(self.assets.values())

    def total_debts(self) -> float:
        return sum(self.debts.values())