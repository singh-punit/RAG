#!/usr/bin/env python3

def calculate_emi(principal, interest_rate, tenure_years):
    """
    Calculate the Equated Monthly Installment (EMI) for a loan.
    
    Args:
        principal: Loan amount (property value)
        interest_rate: Annual interest rate (in percentage)
        tenure_years: Loan tenure in years
    
    Returns:
        Monthly EMI amount
    """
    # Convert annual interest rate to monthly and decimal form
    monthly_interest_rate = interest_rate / (12 * 100)
    
    # Convert tenure from years to months
    tenure_months = tenure_years * 12
    
    # Calculate EMI using the formula: P * r * (1+r)^n / ((1+r)^n - 1)
    # Where P is principal, r is monthly interest rate, and n is tenure in months
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate)**tenure_months
    emi = emi / ((1 + monthly_interest_rate)**tenure_months - 1)
    
    return emi

def main():
    print("===== Loan EMI Calculator =====")
    
    try:
        # Get user inputs
        property_value = float(input("Enter property value: "))
        interest_rate = float(input("Enter annual interest rate (%): "))
        tenure_years = float(input("Enter loan tenure (years): "))
        
        # Validate inputs
        if property_value <= 0 or interest_rate <= 0 or tenure_years <= 0:
            print("Error: All inputs must be positive numbers.")
            return
            
        # Calculate EMI
        monthly_emi = calculate_emi(property_value, interest_rate, tenure_years)
        
        # Display results
        print("\n===== Loan Details =====")
        print(f"Property Value: {property_value:.2f}")
        print(f"Interest Rate: {interest_rate:.2f}%")
        print(f"Loan Tenure: {tenure_years:.1f} years ({int(tenure_years * 12)} months)")
        print(f"Monthly EMI: {monthly_emi:.2f}")
        print(f"Total Amount Payable: {monthly_emi * tenure_years * 12:.2f}")
        print(f"Total Interest Payable: {(monthly_emi * tenure_years * 12) - property_value:.2f}")
        
    except ValueError:
        print("Error: Please enter valid numeric values.")

if __name__ == "__main__":
    main()