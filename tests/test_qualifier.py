# Import pathlib
from pathlib import Path
import csv
from utils.calculators import calculate_monthly_debt_ratio
import pytest


#Import fileio
from utils import fileio

# Import Calculators
from utils import calculators

# Import Filters
from filters.credit_score import filter_credit_score
from filters.debt_to_income import filter_debt_to_income
from filters.loan_to_value import filter_loan_to_value
from filters.max_loan_size import filter_max_loan_size

def test_save_csv():
    # @TODO: Your code here!
    # Use Path from pathlib to output the test csv to ./data/output/qualifying_loans.csv
    csv_file = Path("../data/output.csv")
    bank_data = []
    header = []
    fileio.save_csv(Path("../data/output.csv", bank_data, header))
    assert csv_file.exists()

def test_calculate_monthly_debt_ratio():
    assert calculators.calculate_monthly_debt_ratio(1500, 4000) == 0.375

def test_calculate_loan_to_value_ratio():
    assert calculators.calculate_loan_to_value_ratio(210000, 250000) == 0.84

def test_filters():
    bank_data = fileio.load_csv(Path('../data/daily_rate_sheet.csv'))
    current_credit_score = 750
    debt = 1500
    income = 4000
    loan = 210000
    home_value = 250000
    monthly_debt_ratio = 0.375
    loan_to_value_ratio = 0.84

    # @TODO: Test the new save_csv code!
banks = filter_max_loan_size(loan, bank_data)
print(len(banks))
assert len(banks) == 18
current_credit_score = filter_credit_score(current_credit_score, banks)
assert len(current_credit_score) == 9
test_save_csv(Path('../data/output.csv')).exists()