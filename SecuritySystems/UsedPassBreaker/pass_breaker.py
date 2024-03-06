import time
start_time = time.time()
# List of often-used passwords
password_to_break = ['123456', 'admin', '12345678',
                     '123456789', '1234', '12345',
                     'password', '123', 'Aa123456',
                     '1234567890', 'UNKNOWN', '1234567',
                     '123123', '111111', 'Password',
                     '000000', 'admin123', '********', 'user']

# Initialise the symbols
all_symbols = []
numbers = []
lower_letters = [chr(x) for x in range(ord('A'), ord('a') + 26)]
numbers += [str(x) for x in range(1, 11)]
all_symbols += lower_letters
all_symbols.extend(numbers)


# Breaking algorithm
for password in password_to_break:
    guess = ''
    loops_used = len(password)
    for c in password:
        for s in all_symbols:
            if s == c:
                guess += s
    print(f'Password crashed: {guess}')

print('-----Program Execution------')
print(f"--- {(time.time() - start_time):.10f} seconds ---")

