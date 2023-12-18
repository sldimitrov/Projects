# Def Simple interest
def simple_interest(principal, rate_of_interest, time):
    rate_of_interest = rate_of_interest / 100
    result = (principal * rate_of_interest * time) / 100
    print(result)

# Define func to calculate compound interest
def compound_interest(initial_deposit, interest_rate, time):
    value = initial_deposit * (1 + interest_rate / 100) ** time
    print(value)

# Calculate Loan Payment
# (using the formula for monthly loan payments)
def loan_payment(loan_amount, loan_term, interest_rate):
    ...


# Calculate Future Value of a Savings
# Account (with regular contributions)
def future_value_of_savings(num_of_periods, starting_amount, interest_rate):
    interest_rate = interest_rate / 100
    result = starting_amount * (1 + interest_rate) * num_of_periods
    print(result)


# Implement a main menu function called main_menu
# that displays the following options:
def main_menu():
    print('Main menu operations:')
    print()
    print('1 Calculate Simple Interest')
    print('2 Calculate Compound Interest')
    print('3 Calculate Loan Payment')
    print('4 Calculate Future Value of Savings')
    print('5 Quit the application')
    print('')
    user_input = input(f'Please input a number: ')
    number = int(user_input)
    while number != 5:
        number = int(user_input)
        if number == 5:
            return True
        elif number == 1:
            print('Parameters needed:')
            print('principal, rate_of_interest, time')
            parm1 = float(input())
            parm2 = float(input())
            parm3 = float(input())
            result = simple_interest(parm1, parm2, parm3)
            print(result)
        elif number == 2:
            print('Parameters needed:')
            print('initial_deposit, interest_rate, time')
            parm1 = float(input())
            parm2 = float(input())
            parm3 = float(input())
            result = compound_interest(parm1, parm2, parm3)
            print(result)
        elif number == 3:
            print('Parameters needed:')
            print('loan_amount, loan_term, interest_rate')
            parm1 = float(input())
            parm2 = float(input())
            parm3 = float(input())
            result = loan_payment(parm1, parm2, parm3)
            print(result)
        elif number == 4:
            print('Parameters needed:')
            print('num_of_periods, starting_amount, interest_rate, periodic_deposit')
            parm1 = float(input())
            parm2 = float(input())
            parm3 = float(input())
            parm4 = float(input())
            result = future_value_of_savings(parm1, parm2, parm3)
            print(result)


        print()
        user_input = input(f'Please input a number: ')

main_menu()