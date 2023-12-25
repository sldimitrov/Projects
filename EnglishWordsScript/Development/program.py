# Initialise a file to save the data
words = []
# Read the data from the text file and append it into a list
data = open('list_of_words.txt', 'r')
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    words.append(d)


sentences = []
for word in words:
    print(f'Word or a phrase found: {word}')

    # Collect sentences into a list
    sentence = input('Show imagination: ')
    sentences.append(sentence)
    print('Sentence saved successfully')

    # Remove the word from the words the data
    f = open('list_of_words.txt', 'r')
    text = f.read()
    text = text.replace(word, '')
    f.close()
    f = open('list_of_words.txt', 'w')
    f.write(text)
    f.close()
    print()


# Save the sentences into the data file
file = open('sentences_list.txt', 'w')
file.write('\n'.join(sentences))
file.close()
