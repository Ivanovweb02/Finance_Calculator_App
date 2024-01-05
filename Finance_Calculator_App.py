import math


def simple_interest(num_1: float, num_2: float, num_3: int) -> str:
    calculated_simple_interest = (num_1 * num_2 * num_3) / 100
    return f"Compound Interest: ${calculated_simple_interest :.2f}"


def compound_interest(principal: float, rate: float, time: int) -> str:
    amount = principal * (math.pow((1 + (rate / 100)), time))
    calculated_compound_interest = amount - principal
    return f"Compound Interest: ${calculated_compound_interest :.2f}"


def loan_payment(principal: float, rate: float, time: int) -> str:
    calculated_loan_payment = (principal * rate / 100) / (1 - (1 + rate / 100 / 12) ** (-time * 12))
    return f"Loan Payment: ${calculated_loan_payment :.2f}"


def future_value_of_savings(p: float, r: float, t: int) -> str:
    calculated_future_value = p * (1 + r) ** ((t * 12)-1)/r
    return f"Future Value of Savings: ${calculated_future_value :.2f}"


while True:
    print("Main Menu:")
    print("""
    1. Calculate Simple Interest
    2. Calculate Compound Interest
    3. Calculate Loan Payment
    4. Calculate Future Value of Savings
    5. Quit    
    """)

    choice = input("Enter your choice (1/2/3/4/5):")
    if choice == '1':
        number_1, number_2, number_3 = float(input("Enter principal amount: ")), \
                                       float(input("Enter interest rate (as a decimal): ")), \
                                       int(input("Enter time (in years): "))
        print(simple_interest(number_1, number_2, number_3))
        continue_or_not = input("Do you want to perform another calculation? (yes/no): ")
        if continue_or_not == "yes":
            continue
        elif continue_or_not == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid Text Try Again ! ")

    elif choice == '2':
        number_1, number_2, number_3,  = float(input("Enter principal amount: ")), \
                                       float(input("Enter annual interest rate (as a decimal): ")), \
                                       int(input("Enter time (in years):"))
        print(compound_interest(number_1, number_2, number_3))
        continue_or_not = input("Do you want to perform another calculation? (yes/no): ")
        if continue_or_not == "yes":
            continue
        elif continue_or_not == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid Text Try Again ! ")
    elif choice == '3':
        number_1, number_2, number_3,  = float(input("Enter principal amount: ")), \
                                       float(input("Enter annual interest rate (as a decimal): ")), \
                                       int(input("Enter time (in years):"))
        print(loan_payment(number_1, number_2, number_3))
        continue_or_not = input("Do you want to perform another calculation? (yes/no): ")
        if continue_or_not == "yes":
            continue
        elif continue_or_not == "no":
            print("Goodbye")
            break
        else:
            print("Invalid Text Try Again ! ")
    elif choice == '4':
        number_1, number_2, number_3, = float(input("Enter principal amount: ")), \
                                       float(input("Enter annual interest rate (as a decimal): ")), \
                                       int(input("Enter time (in years): "))
        print(future_value_of_savings(number_1, number_2, number_3))
        continue_or_not = input("Do you want to perform another calculation? (yes/no): ")
        if continue_or_not == "yes":
            continue
        elif continue_or_not == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid Text Try Again ! ")
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid Text Try Again")
