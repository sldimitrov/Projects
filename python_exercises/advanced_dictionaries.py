dabools = [True, False, True, True, False, True, True, False, True, True, False, True, True, False, True,
           True, False, True, True, False, True, True, False, True, True, False, True, True, False, True,
           True, False, True, True, False, True, True, False, True, True, False, True, True, False, True,
           True, False, True, True, False, True, True, False, True, True, False, True, True, False, True,
           True, False, True, True, False, True, True, False, True, True, False, True, True, False, True]

choice_counter = {

}

for choice in dabools:
    if choice not in choice_counter.keys():
        choice_counter[choice] = 0
    else:
        choice_counter[choice] += 1

print("choice_counter", choice_counter)
