print("Loan Repayment Mini Calculator")
loan_amount = float(input("Enter loan amount: "))
monthly_payment = float(input("Enter monthly payment: "))
monthly_interest_rate = float(input("Enter monthly interest rate (%): "))
month = 0
balance = loan_amount
first_month_interest = balance * (monthly_interest_rate / 100)
if monthly_payment <= first_month_interest:
    print("Your monthly payment is too low. The loan will never be paid off.")
else:
    while balance > 0:
        month = month + 1

        interest = balance * (monthly_interest_rate / 100)
        balance = balance + interest - monthly_payment

        if balance < 0:
            balance = 0

        print("Month", month, ": Interest =", round(interest, 2), 
              "Remaining balance =", round(balance, 2))

    print("Loan paid off in", month, "months.")