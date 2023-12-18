
c = input('replace: ')
r = input('with: ')
f = open('text_data/sentences_list.txt', 'r')
text = f.read()
text = text.replace(c, r)
f.close()

f = open('text_data/sentences_list.txt', 'w')
f.write(text)
f.close()


# open the file
# read the file
# replace the word
# close it
