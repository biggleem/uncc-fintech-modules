# Import pathlib
from pathlib import Path

#Import fileio and calculators
from qualifier.utils import (fileio, calculators)

# Import Filters
from qualifier.filters import (
                credit_score,
                debt_to_income,
                loan_to_value,
                max_loan_size)


def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_save_csv():
    csvpath=Path('./data/output/qualifying_loans.csv')
    header=['Lender','Max Loan Amount','Max LTV','Max DTI','Min Credit Score','Interest Rate']
    data=[
        ['Bank of Big - Premier Option',300000,0.85,0.47,740,3.6],
        ['West Central Credit Union - Premier Option',400000,0.9,0.35,760,2.7]
        ]
    assert fileio.save_csv(csvpath,data,header).exists()==True




