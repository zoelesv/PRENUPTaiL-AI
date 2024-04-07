from typing import List
from pydantic import BaseModel
from fastapi.responses import StreamingResponse
from fastapi import APIRouter, Depends, HTTPException, Request, status
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.llms import ChatMessage, MessageRole
from backend.app.engine import get_chat_engine

from app.data_collector.roles import AllPersons
from app.contracts import PrenupAgreement

chat_router = r = APIRouter()


class _Message(BaseModel):
    role: MessageRole
    content: str


class _ChatData(BaseModel):
    messages: List[_Message]


@r.post("")
async def chat(
    request: Request,
    data: _ChatData,
    chat_engine: BaseChatEngine = Depends(get_chat_engine),
):
    # check preconditions and get last message
    if len(data.messages) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No messages provided",
        )
    lastMessage = data.messages.pop()
    if lastMessage.role != MessageRole.USER:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Last message must be from user",
        )
    # convert messages coming from the request to type ChatMessage
    messages = [
        ChatMessage(
            role=m.role,
            content=m.content,
        )
        for m in data.messages
    ]

    # query chat engine
    response = await chat_engine.astream_chat(lastMessage.content, messages)

    # stream response
    async def event_generator():
        async for token in response.async_response_gen():
            # If client closes connection, stop sending events
            if await request.is_disconnected():
                break
            yield token

    return StreamingResponse(event_generator(), media_type="text/plain")


def prompt_template():
    return """

        Purpose and Goals:

        * Act as a legal resource for users by providing information and insights relevant to California prenuptial agreements. 
        * Guide users through the process of creating a prenuptial agreement, highlighting important considerations and legal requirements.
        * Provide clear and objective explanations of legal terminology and concepts related to prenuptial agreements.

        Initial Inquiry:

        a) Begin by explaining that you are a bot specializing in California prenuptial agreements, and are **not a substitute for real legal counsel**.
        b) Ask users if they have any general questions about California prenuptial agreements to assess their level of understanding.
        c) If they lack basic understanding, provide a brief overview of prenuptial agreements and their purpose.

        Agreement Drafting:

        * Guide the user through the process of defining the terms of their prenuptial agreement.
        * Ask about:
            * Assets: Inquire about any separate property each party brings into the marriage (such as real estate, investments, businesses). 
            * Debts: Ask about any existing debts each party carries.
            * Income and Support: Discuss expectations regarding earnings during the marriage, and potential spousal support (alimony) in case of divorce.
            * Other Provisions: Address any other concerns such as inheritance rights, division of pets,  or specific lifestyle choices. 

        Legal Considerations:

        * Emphasize the importance of each party having their own independent legal representation to review the agreement.
        * Remind users that prenuptial agreements must be in writing and signed by both parties to be considered valid. 
        * Inform users about potential grounds for invalidating a prenuptial agreement (e.g., fraud, coercion, or unconscionability).

        Overall Tone:

        * Remain professional and objective throughout your interactions.
        * Use plain language and avoid overly complex legal jargon. Define legal terms when necessary.
        * Be informative and supportive, while always advising users to seek professional legal assistance when needed. 
        
        """


def collect_personal_info(data: _ChatData, aggreement: PrenupAgreement):
    
    # TODO: from chatbot, add all personal info to agreement object.

    # TODO: Retreve actual data from chatbot.
    # for message in data.messages:
    #     if message.role == "user":
    
    aggreement.personal_info.person1.personal_information.first_name=None
    aggreement.personal_info.person2.personal_information.first_name=None
    aggreement.personal_info.person1.personal_information.middle_name=None
    aggreement.personal_info.person2.personal_information.middle_name=None
    aggreement.personal_info.person1.personal_information.last_name=None
    aggreement.personal_info.person2.personal_information.last_name=None
    aggreement.personal_info.person1.personal_information.addresses={"home": None}
    aggreement.personal_info.person2.personal_information.addresses={"home": None}
    aggreement.personal_info.person1.personal_information.phone_numbers={"home": None, "cell": None}
    aggreement.personal_info.person1.personal_information.email_addresses={"home": None}
    aggreement.personal_info.person1.personal_information.marriage_date=None
    aggreement.personal_info.person1.personal_information.marriage_location=None
    aggreement.personal_info.person1.personal_information.religion_affiliation=None
    aggreement.personal_info.person2.personal_information.phone_numbers={"home": None, "cell": None}
    aggreement.personal_info.person2.personal_information.email_addresses={"home": None}
    aggreement.personal_info.person2.personal_information.marriage_date=None
    aggreement.personal_info.person2.personal_information.marriage_location=None
    aggreement.personal_info.person2.personal_information.religion_affiliation=None

    return aggreement


def collect_financial_info(data: _ChatData, aggreement: PrenupAgreement):

    # TODO: from chatbot, add all personal financial info to agreement object.

    # # TODO: Retreve actual data from chatbot.
    # for message in data.messages:
    #     if message.role == "user":
    aggreement.personal_info.person1.finances.tangible_assets=None
    aggreement.personal_info.person2.finances.tangible_assets=None
    aggreement.personal_info.person1.finances.nontangible_assets=None
    aggreement.personal_info.person2.finances.nontangible_assets=None
    aggreement.personal_info.person1.finances.debts=None
    aggreement.personal_info.person2.finances.debts=None
    aggreement.personal_info.person1.finances.income_sources=None
    aggreement.personal_info.person2.finances.income_sources=None
    aggreement.personal_info.person2.finances.financial_obligations=None
    aggreement.personal_info.person2.finances.financial_obligations=None

    return aggreement


def collect_asset_division(data: _ChatData, agreement: PrenupAgreement):
    # Process chat data to determine how assets will be divided
    # Placeholder logic
    agreement.distribution_agreement.asset_division = {"Home": "Person1", "Car": "Person2"}
    return agreement

def collect_debt_division(data: _ChatData, agreement: PrenupAgreement):
    # Process chat data to determine how debts will be divided
    # Placeholder logic
    agreement.distribution_agreement.debt_responsibility = {"Credit Card": "Person1", "Loan": "Person2"}
    return agreement

def collect_spousal_support(data: _ChatData, agreement: PrenupAgreement):
    # Process chat data to determine spousal support details
    # Placeholder logic
    agreement.spousal_support.has_agreement = True
    agreement.spousal_support.amount = 2000  # Monthly amount
    agreement.spousal_support.duration = 24  # Months
    return agreement

def collect_estate_planning(data: _ChatData, agreement: PrenupAgreement):
    # Process chat data for estate planning details
    # Placeholder logic
    agreement.estate_planning.separate_property = {"Heirloom": "Person1"}
    return agreement

def collect_miscellaneous(data: _ChatData, agreement: PrenupAgreement):
    # Process any additional data relevant to the prenuptial agreement
    # Placeholder logic
    # Here you would handle any additional clauses or special considerations
    return agreement

def collect_all_agreement_data(data: _ChatData) -> PrenupAgreement:
    # Initialize a new PrenupAgreement object (or retrieve it if already exists)
    agreement = PrenupAgreement()

    # Call all the individual data collection functions
    collect_personal_info(data, agreement)
    collect_financial_info(data, agreement)
    collect_asset_division(data, agreement)
    collect_debt_division(data, agreement)
    collect_spousal_support(data, agreement)
    collect_estate_planning(data, agreement)
    collect_miscellaneous(data, agreement)

    return agreement


# @chat_router.post("/complete_agreement")
def complete_agreement(data: _ChatData):
    # Here, we assume `agreement` is the PrenupAgreement object filled with all the data collected during the conversation
    agreement = collect_all_agreement_data(data)
    filled_template = populate_template(agreement)
    return {"agreement_text": filled_template}


def populate_template(agreement: PrenupAgreement) -> str:
    # Template string with placeholders for all relevant data
    template = """
    California Prenuptial Agreement Outline
    I. Parties
    A. {person1_name} ("Person1")
    B. {person2_name} ("Person2")

    II. Background
    A. Statement of Intended Marriage
    B. Purpose of the Agreement

    III. Separate Property
    A. Premarital Property of Person1
       Description of Assets and Debts: {person1_assets_and_debts}
    B. Premarital Property of Person2
       Description of Assets and Debts: {person2_assets_and_debts}

    IV. Marital Property
    A. Definition of Marital Property under California Law (Brief Reference)
    B. Treatment of Marital Property During Marriage
       - Community Property with Specific Exceptions: {community_property_exceptions}

    V. Division of Property Upon Divorce or Legal Separation
    A. Separate Property
       1. Person1's Separate Property: {person1_separate_property}
       2. Person2's Separate Property: {person2_separate_property}
    B. Marital Property
       - Specific Allocation of Marital Property: {marital_property_allocation}

    VI. Spousal Support
    A. Conditions for Waiver or Limitation: {spousal_support_conditions}

    VII. Debts and Liabilities
    A. Premarital Debts
       1. Person1's Responsibility: {person1_debts_responsibility}
       2. Person2's Responsibility: {person2_debts_responsibility}
    B. Marital Debts
       - Responsibility Upon Divorce or Legal Separation: {marital_debts_responsibility}

    VIII. Estate Planning Considerations
    A. Inherited Property During Marriage: {inherited_property}
    B. Designation of Beneficiaries for Life Insurance or Retirement Accounts: {beneficiaries_designation}

    IX. Disclosure
    A. Person1's Financial Disclosure Statement: Attached as Exhibit A
    B. Person2's Financial Disclosure Statement: Attached as Exhibit B

    X. Entire Agreement
    A. Supersedes Prior Agreements: {supersedes_prior_agreements}
    B. Binding Effect: {binding_effect}

    XI. Amendments and Revocations
    A. Requirements for Amendments: {amendments_requirements}
    B. Revocation Procedures: {revocation_procedures}

    XII. Severability
    A. Enforceability of Remaining Provisions Despite Invalidity of a Portion: {severability}

    XIII. Independent Legal Counsel
    A. Acknowledgement of Independent Legal Representation: {legal_representation}

    XIV. Voluntary Execution
    A. Signatures and Dates: {signatures_and_dates}

    XV. Exhibits
    A. Person1's Financial Disclosure Statement
    B. Person2's Financial Disclosure Statement

    XVI. Acknowledgement
    A. Acknowledgement of Full Disclosure and Understanding: {full_disclosure}
    """

    # Example of extracting and formatting the data from the agreement
    person1_name = f"{agreement.personal_info.person1.personal_information.first_name} {agreement.personal_info.person1.personal_information.middle_name} {agreement.personal_info.person1.personal_information.last_name}"
    person2_name = f"{agreement.personal_info.person2.personal_information.first_name} {agreement.personal_info.person2.personal_information.middle_name} {agreement.personal_info.person2.personal_information.last_name}"

    # This should be expanded to extract and format all necessary information from the agreement
    person1_assets_and_debts = ', '.join([f"{item}: ${value}" for item, value in agreement.distribution_agreement.asset_division.items()])
    person2_assets_and_debts = ', '.join([f"{item}: ${value}" for item, value in agreement.distribution_agreement.asset_division.items()])

    # The placeholders in the template should be replaced with actual data extracted from the `agreement` object
    filled_template = template.format(
        person1_name=person1_name,
        person2_name=person2_name,
        person1_assets_and_debts=person1_assets_and_debts,
        person2_assets_and_debts=person2_assets_and_debts,
        community_property_exceptions="Specific exceptions here",
        person1_separate_property="Details of Person1's separate property",
        person2_separate_property="Details of Person2's separate property",
        marital_property_allocation="Details of marital property allocation",
        spousal_support_conditions="Conditions for spousal support",
        person1_debts_responsibility="Details of Person1's debt responsibility",
        person2_debts_responsibility="Details of Person2's debt responsibility",
        marital_debts_responsibility="Responsibility for marital debts",
        inherited_property="Details of inherited property",
        beneficiaries_designation="Details of beneficiaries designation",
        supersedes_prior_agreements="Details of superseding prior agreements",
        binding_effect="Details of binding effect",
        amendments_requirements="Requirements for amendments",
        revocation_procedures="Revocation procedures",
        severability="Details of severability",
        legal_representation="Details of legal representation",
        signatures_and_dates="Signatures and dates details",
        full_disclosure="Details of full disclosure"
        # Continue with other fields as necessary...
    )

    return filled_template
