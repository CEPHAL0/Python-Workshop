# Bank Loan Eligibility Calculator

# Conditions

# Age > 21
# Monthly Salary should be at least 10% of loan amount
# Chosen Interest Rate should not be less than 13%

# Age > 40
# Monthly Salary at least 50% of loan amount

# Input -> Age, Monthly salary, loan amount, interest rate
# Output -> Eligible / Not Eligible


age = int(input("Enter the age: "))
monthly_salary = float(input("Enter the monthly salary: "))
loan_amount = float(input("Enter the loan amount: "))
interest_rate = float(input("Enter the interest rate: "))

age_greater_than_21 = age > 21
monthly_salary_10 = monthly_salary >= (0.1 * loan_amount)
interest_rate_13 = interest_rate >= 13

age_greater_than_40 = age > 40
monthly_salary_50 = monthly_salary >= (0.5 * loan_amount)

eligibility = (age_greater_than_21 and monthly_salary_10 and interest_rate_13) or(age_greater_than_40 and monthly_salary_50)

if eligibility:  # Shortcut for -> if eligibility == True:
    print("Eligible")
else:
    print("Not Eligible")