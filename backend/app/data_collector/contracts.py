from dataclasses import dataclass
from app.data_collector.persons import AllPersons
from app.data_collector.distribution_agreement import DistributionAgreement, SpousalSupport, EstatePlanning

@dataclass
class PrenupAgreement:
    personal_info: AllPersons
    distribution_agreement: DistributionAgreement
    spousal_support: SpousalSupport
    estate_planning: EstatePlanning
    legal_representation_reviewed: bool

    
    def legal_representation_review(self):
        self.legal_representation_reviewed = True