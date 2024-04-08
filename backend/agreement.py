def get_agreement(chat):
    """Create and return the agreement text based on the chat.

    chat: The ChatSession
    """
    response = chat.send_message("""Here is the outline of the agreement:

------------------------------------------------------------------------

I. Parties

A. [Name of Wife] ("Wife")
B. [Name of Husband] ("Husband")

II. Background

A. Statement of Intended Marriage
B. Purpose of the Agreement

III. Separate Property

A. Premarital Property of Wife
Description of Assets and Debts
Characterization as Separate Property
B. Premarital Property of Husband
Description of Assets and Debts
Characterization as Separate Property

IV. Marital Property

A. Definition of Marital Property under California Law (Brief Reference)
B. Treatment of Marital Property During Marriage (Optional - Choose One)
Community Property with Specific Exceptions (List Exceptions)
Specific Agreements Regarding Income and Expenses

V. Division of Property Upon Divorce or Legal Separation

A. Separate Property
Wife's Separate Property
Husband's Separate Property
B. Marital Property (Choose One)
Standard California Community Property Division
Specific Allocation of Marital Property (List Specific Items and Allocation)

VI. Spousal Support

A. Waiver or Limitation of Spousal Support (Optional)
Conditions for Waiver or Limitation
Minimum or Maximum Spousal Support (if applicable)

VII. Debts and Liabilities

A. Premarital Debts
Wife's Premarital Debts - Responsibility
Husband's Premarital Debts - Responsibility
B. Marital Debts
Responsibility During Marriage
Responsibility Upon Divorce or Legal Separation

VIII. Estate Planning Considerations (Optional)

A. Inherited Property During Marriage
B. Designation of Beneficiaries for Life Insurance or Retirement Accounts (if applicable)

IX. Disclosure

A. Wife's Financial Disclosure Statement (Attached as Exhibit A)
B. Husband's Financial Disclosure Statement (Attached as Exhibit B)

X. Entire Agreement

A. Supersedes Prior Agreements
B. Binding Effect

XI. Amendments and Revocations

A. Requirements for Amendments
B. Revocation Procedures

XII. Severability

A. Enforceability of Remaining Provisions Despite Invalidity of a Portion

XIII. Independent Legal Counsel

A. Acknowledgement of Independent Legal Representation

XIV. Voluntary Execution

A. Signatures and Dates

XV. Exhibits

A. Wife's Financial Disclosure Statement
B. Husband's Financial Disclosure Statement

XVI. Acknowledgement

A. Acknowledgement of Full Disclosure and Understanding

------------------------------------------------------------------------

Generate text for section I. Be sure to include the section title.""").text

    for section in ['II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI']:
        response += '\n\n' + chat.send_message('Generate text for section %s. Be sure to include the title of the section.' % section, safety_settings={'HARASSMENT':'block_none'}).text
    return response
