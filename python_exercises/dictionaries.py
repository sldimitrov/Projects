words = ['abc', 'cba', 'adxad']

definitions = ['list of', 'dictionaries']

cooldictionary = {}

for i in range(len(words)):
    if not (0 <= i < len(words)) or not (0 <= i < len(definitions)):
        break

    cooldictionary[words[i]] = definitions[i]

print(cooldictionary)
