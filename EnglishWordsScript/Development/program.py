# Initialise a file to save the data
lines = []
# Read the data from the text file and append it into a list
data = open('list_of_words.txt', 'r')
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    lines.append(d)


words = []
definitions = []
sentences = []
for line in lines:
    print(f'Word or a phrase found: {line}')

    # Collect sentences into a list
    sentence = input('Show imagination: ')
    sentences.append(sentence)
    print('Sentence saved successfully')

    # Split the line by ("-")
    word, definition = line.split(' - ')

# Save the sentences into the data file
file = open('sentences_list.txt', 'w')
file.write('\n'.join(sentences))
file.close()
