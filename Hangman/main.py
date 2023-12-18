import random
parts_of_body = ['head', 'stomach', 'knee', 'hearth', 'the smallest toe', 'between the eyes']
is_won = False


def chose_word(user_input: str):
    country = ["Bulgaria", "France", "Germany", "Italy", "Spain", "Belgium", "Denmark", "Netherlands", "Norway",
                 "Poland",
                 "Portugal", "Turkey", "Romania", "Serbia", "Slovakia", "Slovenia", "Moldova", "Russia", "Latvia",
                 "Malta"]
    capitals = ["Sofia", "Paris", "Berlin", "Rome", "Madrid", "Brussels", "Copenhagen", "Amsterdam", "Oslo", "Warsaw",
                "Lisbon", "Ankara", "Bucharest", "Belgrade", "Bratislava", "Moscow", "Valletta"]
    football_clubs = ["CSKA", "PSG", "Bayren", "Inter", "Barcelona", "Gent", "Ajax", "Legia", "Galatasaray", "Porto",
                      "Partizan", "Spartak", "Real", "Milan", "Juventus", "Liverpool", "Arsenal", "Levski", "Valencia"]

    if user_input == 'country':
        word = random.choice(country)
        return word
    elif user_input == 'capitals':
        word = random.choice(capitals)
        return word
    elif user_input == 'football_clubs':
        word = random.choice(football_clubs)
        return word
    return None


while True:
    category = input('\nThis is HangmanGangstaEdition\n'
                     '   Please choose a category\n'
                     'country/capitals/football_clubs: ').lower()
    if category not in ['country', 'capitals', 'football_clubs']:
        print(f'\nYou received bullet in the {random.choice(parts_of_body)}\n'
              f'      try again...')
    else:
        break


chosen_word = chose_word(category)
if chosen_word is not None:
    print(f'\nChosen category is {category}.')
    current_category = ['_'] * len(chosen_word)
    current_letters = []
    attempts = 10

    while attempts > 0:
        print("Word: ", " ".join(current_category))
        print(f'Attempts left: {attempts}')

        input_letter = input('Write a letter, you know: ')
        if len(input_letter) > 1 or not input_letter.isalpha():
            print('\nInput just one letter boy:')
            continue

        if input_letter in current_category:
            print('\nYou already got this letter, bad boy,\n'
                  'that means minus attempt! Try with another one:')
            attempts -= 1
            continue

        if input_letter not in chosen_word.lower():
            print('\nIncorrect answer, sorry bruda, attempts -1...\n')
            attempts -= 1

        else:
            current_letters.append(input_letter)
            if input_letter in chosen_word.lower():
                for i in range(len(chosen_word)):
                    if chosen_word.lower()[i] == input_letter:
                        current_category[i] = input_letter

        if ''.join(current_category).capitalize() == chosen_word:
            is_won = True
            break

if is_won:
    print(f'Congratulations manqk, you found the chosen word - {chosen_word}, successfully!')
else:
    print(f'Sorry broski, you could not guess the {category} - {chosen_word}')



