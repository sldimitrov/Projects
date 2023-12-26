import random


def write_sentences() -> bool:
    """
    This function has 3 main functionalities.
    1-st: Save the words from (words text file) into a list.
    2-nd: Allows you to write a sentence for every word and it automatically
    saves it into (sentences text file).
    3-rd: Saves every passed word into a dictionary with its definition.
    The purpose behind this last action is to make sure that you will be able
    to access all of the words you had learned - with (show_new_word) function
    """
    lines = []

    # Read the data from the text file and append it into a list
    data = open('list_of_words.txt', 'r')
    for d in data:
        if '\n' in d:
            d = d.replace('\n', '')
        lines.append(d)

    words_dictionary = {}
    sentences = []
    for line in lines:
        if line:  # if it's not a blank line
            # Split the line by ("-") in order to get the word and its definition
            word, definition = line.split('-')
            print(f'\nWord or a phrase found: {word}')
            print(f'Definition: {definition}')

            # Collect sentences into a list
            sentence = input('Show imagination: ')
            sentences.append(sentence)
            print('Sentence saved successfully')

            # Save the word with its definition into a dictionary
            words_dictionary[word] = definition

            # Remove the written words from the (words text file)
            f = open('./list_of_words.txt', 'r')
            text = f.read()
            text = text.replace(line, '')
            f.close()
            f = open('./list_of_words.txt', 'w')
            f.write(text)
            f.close()
            print()

    # Save the sentences into a text file
    file = open('./sentences_list.txt', 'a')
    file.write('\n')
    file.write('\n'.join(sentences))
    file.close()

    # Save the words and their definitions into the dictionary
    file = open('./dictionary.txt', 'a')
    for key, value in words_dictionary.items():
        file.write(f'{key} - {value}\n')
    file.close()
    return True


def access_dictionary() -> bool:
    f = open('./dictionary.txt', 'r')
    data = f.read()
    for _ in data:
        if _.isalpha():
            print(data)
            f.close()
            return True
    else:
        print('There are not any words in the dictionary')
        return True


def show_new_words() -> bool:
    f = open('./list_of_words.txt', 'r')
    data = f.read()
    for _ in data:
        if _.isalpha():
            print('\nList of all new words:')
            print(data)
            f.close()
            return True
    else:
        print('There are not any new words.')   # ADD A OPERATION - ADDING NEW WORDS WHEN THE LIST IS EMPTY
        return True


def test_knowledge():
    data = open('dictionary.txt', 'r')   # Open the text file
    lines = []
    # Remove all the new lines from the data in order to save each line in a list
    if data:  # Save the data into a list
        for d in data:
            if '\n' in d:
                d = d.replace('\n', '')
            if d:
                lines.append(d)

        # Let the User to choose a game type
        answer = input('Here you will be able to check your knowledge.\n'
                       'Please choose a game-type\n'
                       '(s) for a short one\n'
                       'and (l) for a longer one'
                       '...')
        if answer == 's':
            n = 10
        elif answer == 'l':
            n = 20
        else:
            print('Error: Invalid Input')
            return True

        # Choose a random word from the list and ask the user for its definition
        points = 0
        bad_words = []
        for _ in range(n):
            number = random.randint(0, len(lines) - 1)
            line = lines[number]
            word, definition = line.split('-')
            print(f'\nThe given words is: {word}')
            back = input('What is the definition?: ')

            print(f'\nThe definition is: {definition}')
            signal = input('Did you answer correctly? (y/n): ')
            if signal.lower() == 'y':
                points += 1
                print('+1 point')
            elif signal.lower() == 'n':
                bad_words.append(line)

        if answer == 's':
            if points <= 3:
                print('\nYou still have much to learn, buddy!\n'
                      f'Points: {points}:10')
            elif 3 < points <= 5:
                print('\nYou are in the middle gold, motivate yourself to do better!\n'
                      f'Points: {points}:10')
            elif 5 < points <= 8:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}:10')
            elif 8 < points <= 10:
                print('\nExcellent!\n'
                      f'Points: {points}:10')

        elif answer == 'l':
            if points <= 6:
                print('\nYou still have much to learn, buddy!\n'    
                      f'Points: {points}/20')
            elif 6 < points <= 10:
                print('\nYou are in the middle gold, motivate yourself to do better!\n' 
                      f'Points: {points}/20')
            elif 10 < points <= 16:
                print('\nGood job! Keep learning!\n'
                      f'Points: {points}/20')
            elif 16 < points <= 20:
                print('\n'
                      'Excellent! -------\n'              
                      f'Points: {points}/20\n'
                      f'------------------')
        else:
            print('Wrong game-type inputted')
            return True
        return True

    else:   # No words in the dictionary:
        print('There are not any words in your dictionary.')
        menu()


def show_info():
    message = '\tEverything you need to know\n' \
              'This program was born in my head and it was implemented into code by my own hands.\n\n' \
              '  The mission:\n' \
              'To help others. Learning never stops and it makes us better humans. This is the main purpose,\n' \
              'for which I managed to create something, that will help us to be and earn more!\n\n' \
              '  How to use it?\n' \
              'Everything in this program is separated into sections.\n' \
              ' Let\'s say that you\'d just inputted the words, that you want to write\n' \
              'into the (list of words txt) - This is when you want to choose (1)\n' \
              ' On the other hand, when you had already used this program at least once.\n' \
              'You\'re not sure which words you have in your text file, choose (2) and find out.\n'\
              ' Moreover, if you want to see which words you have already learned input (3)\n' \
              ' Within the forth operation (4) you are not only going to learn. You\'re going to be challenged!\n' \
              'Choose it and go and face your demons or stay the same forever!\n' \
              ' (5) is what you had already chosen, so I believe it does not need any explanation\n' \
              ' If information is all you needed at this point choose (6) to exit the temple.\n' \
              'I will be waiting for your return, because I hope that your learning will be an endless process!'
    return message


def menu() -> str:
    """
    This function will contain only the user menu
    """
    menu_message = ('Please, choose an operation (1/2/3/4/5/6):\n'
                    '1. Write down new sentences\n'
                    '2. See the new words\n'
                    '3. Open the dictionary\n'
                    '4. Test your knowledge\n'
                    '5. Info\n'
                    '6. Exit the program')
    return menu_message


# This and the other 2 functions below are responsible for the input
def get_input() -> str:
    """
    When called: This function prints out a message, which asks the user to input a single number.
    Then: Check if user's input is valid by calling the (input validator) function and if its not -
    calls out the (handle invalid input) which prints out an Error message.
    :return: str
    """
    while True:
        choice = input('\nChoose operation (1/2/3/4/5/6) or (m) if you want to see the menu: ')
        if choice is input_validator(choice):
            print(handle_invalid_input(choice))
        else:
            return choice


def input_validator(message: str):
    """
    This functions checks if the choice of the user occurs in the valid list of answers
    If not: the (handle invalid input) func. is being called.
    :param message: str
    :return: str / bool
    """
    valid_answers = [1, 2, 3, 4, 5, 6]
    if message not in valid_answers:
        message = handle_invalid_input(message)
        return message
    return True


def handle_invalid_input(some_input: str):
    """
    Returns an error message every time it is called
    :param some_input: str
    :return: str
    """
    return f'Error: {some_input} is an invalid input\n'


def main():
    """
    This function contains the  of the entire program.
    It will call other functions when the user needs them.
    """
    print(menu())
    choice = get_input()
    while True:
        if choice == 'm':
            main()
        choice = int(choice)
        if choice == 1:
            write_sentences()
        elif choice == 2:
            show_new_words()
        elif choice == 3:
            access_dictionary()
        elif choice == 4:
            test_knowledge()
        elif choice == 5:
            print(show_info())
        elif choice == 6:
            break
        choice = get_input()


print(' Hello, Learner!\n'
      'Are you ready to dive into a world fulfilled with new words and meanings?\n')

if __name__ == '__main__':
    main()

print('\nThank yourself for the time you spent learning!\n'
      'I am so happy that you just used my program!\n'
      'If you had seen any bugs or if you have any ideas\n'
      'how I should improve my app, please mail me here:\n'
      ' -slavidimitrov54@gmail.com\n'
      '                             Best wishes,\n'
      '                             Slavi Dimitrov')

