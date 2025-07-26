# Loan EMI Calculator

A comprehensive Python application to calculate Equated Monthly Installments (EMI) for loans with detailed financial breakdown.

## Files

- `loan_emi_calculator.py` - Complete EMI calculator with user interface

## Features

- **EMI Calculation**: Uses the standard EMI formula
- **Input Validation**: Ensures all inputs are positive numbers
- **Detailed Output**: Shows loan details, total payable amount, and interest
- **Error Handling**: Graceful handling of invalid inputs
- **User-Friendly Interface**: Interactive command-line interface

## Formula Used

```
EMI = P × r × (1+r)^n / ((1+r)^n - 1)
```

Where:

- P = Principal loan amount
- r = Monthly interest rate (annual rate / 12 / 100)
- n = Tenure in months

## Usage

```bash
cd loan-emi-calculator
python3 loan_emi_calculator.py
```

## Example

```
===== Loan EMI Calculator =====
Enter property value: 1000000
Enter annual interest rate (%): 8.5
Enter loan tenure (years): 20

===== Loan Details =====
Property Value: 1000000.00
Interest Rate: 8.50%
Loan Tenure: 20.0 years (240 months)
Monthly EMI: 8678.23
Total Amount Payable: 2082774.40
Total Interest Payable: 1082774.40
```

## Applications

- Home loan calculations
- Personal loan planning
- Car loan EMI estimation
- Financial planning and budgeting
- Loan comparison analysis

## Validation

- Checks for positive numeric inputs
- Handles invalid data gracefully
- Provides clear error messages
