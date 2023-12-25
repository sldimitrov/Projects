# Initialise a file to save the data
words = []
# Read the data from the text file
data = open('text_data/list_of_words.txt', 'r')
# Append the data into a list
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    words.append(d)
print(words)

# find every character from the alphabet
alphabet = [chr(x) for x in range(97, 97 + 26)]
print(alphabet)


# Operations with the output
sentences = []
letter = 0
while letter < 2:
    words_startswith = []
    print(f'Current letter: {alphabet[letter]}')
    # Loop through the list
    for word in words:
        if word.startswith(alphabet[letter]):  # if match
            print(f'Word or a phrase found: {word}')

            # Collect sentences into a list
            sentence = input('Show imagination: ')
            sentences.append(sentence)
            print('Sentence saved successfully')

            # Remove the word from the words the data
            f = open('text_data/list_of_words.txt', 'r')
            text = f.read()
            text = text.replace(word, '')
            f.close()
            f = open('text_data/list_of_words.txt', 'w')
            f.write(text)
            f.close()
            print()
    # Go up to the next letter
    letter += 1

# Save the sentences into the data file
file = open('text_data/sentences_list.txt', 'w')
file.write('\n'.join(sentences))
file.close()
