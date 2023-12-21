# Define a function
def multiply(a: int, b: int):
    """
    Function for multiply two int parameters
    :return: multiplication
    """
    return a * b

def divide(a: int, b: int):
    """
    Functiont for divide two int parameters
    :return: division
    """
    return a / b

def add(a: int, b: int):
    """
    Functiont for adding two int parameters
    :return: addition
    """
    return a + b

def subtract(a: int, b: int):
    """
    Function for subtract two int parameters
    :return: subtraction
    """
    return a - b

def main(operator: str, a: int, b: int):
    """
    This function takes a operator and 2 float numbers.
    Based on the operator it calls a function which
    calculates the result
    """
    if operator == 'multiplication':
        result = multiply(a, b)
    elif operator == 'division':
        result = divide(a, b)
    elif operator == 'addition':
        result = add(a, b)
    elif operator == 'subtraction':
        result = subtract(a, b)
    return result

print('Python Calculator')

print('Menu:')
print()
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Division')
print('5.Quit')

quiting = False
while True:
    if quiting:
        break
    choice = input('Enter your choice (1/2/3/4/5) ')
    choice = int(choice)
    if 1 <= choice <= 5:
        while True:
            choice = int(choice)
            if choice == 1:
                choice = 'Addition'.lower()
            elif choice == 2:
                choice = 'Subtraction'.lower()
            elif choice == 3:
                choice = 'Multiplication'.lower()
            elif choice == 4:
                choice = 'Division'.lower()
            elif choice == 5:
                quiting = True
                break
            print()
            a = int(input('Enter the first number: '))
            b = int(input('Enter the second number: '))
            if choice != "division" and b != 0:
                print(main(choice, a, b))
            else:
                print('Error: Division by zero')

            choice = input('Enter your choice (1/2/3/4/5) ')
    else:
        print('Error: Incorrect operation chosen')

print('Goodbye!')