# Import pathlib
from pathlib import Path

#Import fileio
from qualifier.utils import fileio

# Import Calculators
from qualifier.utils import calculators

# Import Filters
from qualifier.filters import (
        credit_score,
        debt_to_income,
        loan_to_value,
        max_loan_size)

"""
Script to test the filter functionality of the individual functions in the 
filters.py script refererred in the import above.

The selected sample data input is in "loan_data_for_testing", which is an static list of list 
of a subset of lenders loan condition extracted from a "data/daily_rate_sheet.csv". 
Conditions are defined to confirm whether each filter will effectively eliminate 
(or not) some rows from the static input. One condition per each has been provided.
"""

# SECTION 1: Sample unfiltered data, and filtered data results expected in each test
        # 1.0 Sample unfiltered data in all test
loan_data_for_testing=[
# Lender name                   max_loan_amount  max_ltv  max_dti  min_credit_score  
['Bank of Fintech - Starter Plus',	 100000,    0.85,   0.47,	610],
['FHA Fredie Mac - Starter Plus',	 300000,    0.85,   0.45,	550],
['FHA Fredie Mac - Premier Option',	 600000,    0.9,    0.43,	790],
['General MBS Partners - Premier Option',400000,   0.95,    0.35,	790]
]

        # 1.1 Filtered data by credit score approval (credit_score=650)
credit_score_approval=[
# Lender name                   max_loan_amount  max_ltv  max_dti  min_credit_score  
['Bank of Fintech - Starter Plus',	100000,	   0.85,   0.47,	610],
['FHA Fredie Mac - Starter Plus',	300000,    0.85,   0.45,	550]
]

        # 1.2 Filtered data by debt to income ratio approval (DTI=0.46)
debt_to_income_approval=[
# Lender name                   max_loan_amount  max_ltv  max_dti  min_credit_score  
['Bank of Fintech - Starter Plus',	 100000,    0.85,   0.47,	610]
]

       # 1.3 Filtered data by loan to value ratio approval. (LTV=0.7)
loan_to_value_approval=loan_data_for_testing

       # 1.4 Filtered data by loan to value ratio approval (Loan amount=$700,000.-)
max_loan_amount_approval=[]

# 2. TESTS
def test_filter_credit_score():
        assert credit_score.filter_credit_score(620, loan_data_for_testing)==credit_score_approval

def test_filter_debt_to_income():
        assert debt_to_income.filter_debt_to_income(0.46, loan_data_for_testing)==debt_to_income_approval

def test_filter_loan_to_value():
        assert loan_to_value.filter_loan_to_value(0.7,loan_data_for_testing)==loan_to_value_approval

def test_filter_max_loan_size():
        assert max_loan_size.filter_max_loan_size(700000,loan_data_for_testing)==[]

