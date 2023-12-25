def write_sentences():
    """
    This function has offers 3 main functionalities.
    They are:
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
            print(f'Word or a phrase found: {word}')
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


def access_dictionary():
    f = open('./dictionary.txt', 'r')
    data = f.read()
    print(data)
    f.close()


def show_new_words():
    f = open('./list_of_words.txt', 'r')
    data = f.read()
    if data:
        print('\nList of all new words:')
        print(data)
        f.close()
    else:
        print('There are not any new words.')   # ADD A OPERATION - ADDING NEW WORDS WHEN THE LIST IS EMPTY


def test_knowledge():
    ...


def show_info():
    ...


def menu():
    """
    This function will contain only the user menu
    """
    print('Please, choose an operation (1/2/3/4/5/6):\n'
          '1. Write down new sentences\n'
          '2. See the new words\n'
          '3. Open the dictionary\n'
          '4. Test your knowledge\n'
          '5. Info\n'
          '6. Exit the program')


# This and the other 2 functions below are responsible for the input
def get_input():
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
    menu()
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
            show_info()
        elif choice == 6:
            test_knowledge()
        choice = get_input()


print(' Hello, Learner!\n'
      'Are you ready to dive into a world fulfilled with new words and meanings?\n')

if __name__ == '__main__':
    main()

print('Thank yourself for the time you spent learning!\n'
      'We are so happy that you just used our program!\n'
      'If you had detected any bugs or if you just have any ideas\n'
      'how we should improve our app, please mail us here:\n'
      '\tslavidimitrov54@gmail.com')

