# Define a function
def multiply(a: int, b: int):
    """
    Function for multiply two int parameters
    :return: multiplication
    """
    return a * b


def divide(a: int, b: int):
    """
    Function for divide two int parameters
    :return: division
    """
    return a / b


def add(a: int, b: int):
    """
    Function for adding two int parameters
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
        print('Addition:')
        result = add(a, b)
    elif operator == 'subtraction':
        result = subtract(a, b)
    return result


def menu():
    print('Python Calculator')
    print('Menu:')
    print()
    print('1.Addition')
    print('2.Subtraction')
    print('3.Multiplication')
    print('4.Division')
    print('5.Menu')
    print('6.Quit')
    return True


quiting = False
while True:
    if quiting:
        break
    choice = input('Enter your choice (1/2/3/4/5/6): ')
    choice = int(choice)
    if 1 <= choice <= 5:
        while True:
            choice = int(choice)
            if choice == 1:
                choice = 'addition'
            elif choice == 2:
                choice = 'subtraction'
            elif choice == 3:
                choice = 'multiplication'
            elif choice == 4:
                choice = 'division'
            elif choice == 5:
                menu()
            elif choice == 6:
                exit()
            choice = input('Enter your choice (1/2/3/4/5): ')
    else:
        print('Error: Incorrect operation chosen')

print('Thank you for using our program!\n Goodbye!')