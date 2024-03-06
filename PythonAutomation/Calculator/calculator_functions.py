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


def get_numbers():
    a = int(input('Enter the first number: '))
    b = int(input('Enter the second number: '))
    return a, b


def operations(operator: str) -> float:
    """
    This function takes a operator and 2 float numbers.
    Based on the operator it calls a function which
    calculates the result
    """
    print(f'  \t{operator.title()}')
    if operator == 'multiplication':
        a, b = get_numbers()
        result = multiply(a, b)
    elif operator == 'division':
        a, b = get_numbers()
        if b != 0 and b > 0:
            result = divide(a, b)
        else:
            result = 'Error: you cannot divide by 0'
    elif operator == 'addition':
        a, b = get_numbers()
        result = add(a, b)
    elif operator == 'subtraction':
        a, b = get_numbers()
        result = subtract(a, b)
    elif operator == 'menu':
        menu()
        result = ''
    else:
        print('Wrong operator used')
        return False
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


def main():
    menu()
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
                choice = 'menu'
            elif choice == 6:
                answer = input('Are you sure you want to exit the program? (y/n): ')
                if answer == 'y':
                    exit()
                else:
                    pass
            else:
                print('Error: wrong operator used.')
            print(operations(choice))
            choice = input('Enter your choice (1/2/3/4/5/6): ')


if __name__ == '__main__':
    main()

print('Thank you for using our program!\n Goodbye!')