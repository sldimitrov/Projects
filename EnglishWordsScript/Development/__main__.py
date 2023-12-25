def write_sentences():
    # Initialise a file to save the data
    lines = []
    # Read the data from the text file and append it into a list
    data = open('list_of_words.txt', 'r')
    for d in data:
        if '\n' in d:  # Removes new lines
            d = d.replace('\n', '')
        lines.append(d)

    words_dictionary = {}
    sentences = []
    for line in lines:
        if line:
            print(f'Word or a phrase found: {line}')

            # Collect sentences into a list
            sentence = input('Show imagination: ')
            sentences.append(sentence)
            print('Sentence saved successfully')

            # Split the line by ("-")
            word, definition = line.split('-')
            words_dictionary[word] = definition

            # remove words
            f = open('list_of_words.txt', 'r')
            text = f.read()
            text = text.replace(line, '')
            f.close()
            f = open('list_of_words.txt', 'w')
            f.write(text)
            f.close()
            print()

    # Save the sentences into the data file
    file = open('sentences_list.txt', 'a')
    file.write('\n')
    file.write('\n'.join(sentences))
    file.close()

    file = open('dictionary.txt', 'a')
    for key, value in words_dictionary.items():
        file.write(f'{key} - {value}\n')
    file.close()


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

