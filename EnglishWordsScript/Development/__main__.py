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
            print(f'Word or a phrase found: {line}')

            # Collect sentences into a list
            sentence = input('Show imagination: ')
            sentences.append(sentence)
            print('Sentence saved successfully')

            # Split the line by ("-") in order to get the word and its definition
            word, definition = line.split('-')
            words_dictionary[word] = definition

            # Remove the written words
            f = open('list_of_words.txt', 'r')
            text = f.read()
            text = text.replace(line, '')
            f.close()
            f = open('list_of_words.txt', 'w')
            f.write(text)
            f.close()
            print()

    # Save the sentences into a text file
    file = open('sentences_list.txt', 'a')
    file.write('\n')
    file.write('\n'.join(sentences))
    file.close()

    # Save the words and their definitions into the dictionary
    file = open('dictionary.txt', 'a')
    for key, value in words_dictionary.items():
        file.write(f'{key} - {value}\n')
    file.close()
    return True


def access_dictionary():
    ...


def show_new_words():
    ...


def test_knowledge():
    ...


def menu():
    """
    This function will contain only the user menu
    """
    answer = input('Hello User!\n'
                   'Please, choose an operation (1/2/3/4):\n'
                   '1. To write down new sentences\n'
                   '2. Open the dictionary\n'
                   '3. To see the new words\n'
                   '4. To test your knowledge\n'
                   '...')

    valid_answers = [1, 2, 3, 4]
    answer = int(answer)
    if answer not in valid_answers:
        return f'Error: Invalid choice input...'
    return answer


def main():
    """
    This function will contain the structure of the entire program.
    It will call other functions when the user needs them.
    """
    choice = menu()
    if len(choice) > 2:
        print(choice)
        main()
    elif choice == 1:
        write_sentences()
    elif choice == 2:
        access_dictionary()
    elif choice == 3:
        show_new_words()
    elif choice == 4:
        test_knowledge()


if __name__ == '__main__':
    main()

