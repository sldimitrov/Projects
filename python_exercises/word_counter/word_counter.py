# Read and split the words
f = open("text.txt")

data = f.read()

words = data.split(" ")

# Helper function
def word_formatter(word: str):
    return "".join(l for l in word if l.isalnum())

# print(words)

# Define word counter
word_counter = {}

# Map through data
for idx, word in enumerate(words):
    formatted_word = word_formatter(word)

    if formatted_word not in word_counter.keys():
        word_counter[formatted_word] = 1
        continue

    word_counter[formatted_word] += 1

# TODO: Sort results
sorted_counter = {v for key, v in sorted(word_counter.items(), key=lambda item: item[1])}

# Print results
for count_result in sorted_counter:
    print(f"{count_result} - {word_counter[count_result]}")
