def classify_interest_rate(interest_rate):
    if interest_rate < 0:
        return "Invalid interest rate"
    elif interest_rate < 0.5:
        return "Low interest rate"
    elif interest_rate < 1.5:
        return "Moderate interest rate"
    else:        
        return "High interest rate"    
try:
    interest_rate = float(input("Enter the interest rate: "))
    result = classify_interest_rate(interest_rate)
    print(result)
except:
    print("Invalid input.")