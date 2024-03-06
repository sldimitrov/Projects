import hashlib


# Define the main function
def main_func():  # TODO Documentation
    print('Hello, User!\n')
    text = input('Please input a simple or more complex string here: ')
    print('\nWell done, now you have three options,\n'
          'first one - search or replace what is in\n'
          'the string using the build-in string methods.\n'
          'second one - see what is inside using some\n'
          'other string methods.\n'
          'third one - decrypt it with secret encoding algorithm\n')
    choice = int(input('Please, input your choice ( 1 / 2 / 3 ), here: '))
    if choice == 1:
        search_and_replace(text)
    elif choice == 2:
        what_is_inside(text)
    elif choice == 3:
        encrypt_msg(text)


def search_and_replace(string: str):  # TODO All cases and while loops
    print('list of methods: ( find | count | startswith | endswith )')
    choice = input('\nPlease, enter your chosen one: ')
    if choice == 'find':
        pass
    elif choice == 'count':
        pass
    elif choice == 'startswith':
        pass
    elif choice == 'endswith':
        pass
    else:
        print('Error: 404 | Lack of Education')


def what_is_inside(string: str):
    print('list of methods: ( isdigit | isdecimal | isnumeric| isalpha | isspace| isalnum | islower | isupper )')
    choice = input('\nPlease, enter your chosen one: ')
    if choice == 'isdigit':
        pass
    elif choice == 'isdecimal':
        pass
    elif choice == 'isnumeric':
        pass
    elif choice == 'isalpha':
        pass
    elif choice == 'isspace':
        pass
    elif choice == 'isalnum':
        pass
    elif choice == 'islower':
        pass
    elif choice == 'isupper':
        pass
    else:
        print('Error: 404 | Lack of Education')


def encrypt_msg(string: str):
    string = string.encode()
    hash = hashlib.md5(string)
    print(f"Your encrypted message -> -> -> \n{hash.digest()}  <- <- <-")




main_func()