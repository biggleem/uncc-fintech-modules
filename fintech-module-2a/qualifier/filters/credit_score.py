# -*- coding: utf-8 -*-
"""Credit Score Filter.

This script filters a bank list by the user's minimum credit score.

"""


def filter_credit_score(credit_score, bank_list):
    """Filters the bank list by the mininim allowed credit score set by the bank.

    Args:
        credit_score (int): The applicant's credit score.
        bank_list (list of lists): The available bank loans.

    Returns:
        A list of qualifying bank loans.
    """

    credit_score_approval_list = []
    for bank in bank_list:
        if credit_score >= int(bank[4]):
            credit_score_approval_list.append(bank)
    return credit_score_approval_list
