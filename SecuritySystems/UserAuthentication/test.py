from cryptography.fernet import Fernet


def register_credentials(username, password, credentials):
    # generate a key for encryption and decryption
    # You can use fernet to generate
    # the key or use random key generator
    # here I'm using fernet to generate key

    key = Fernet.generate_key()
    print(key)

    # Instance the Fernet class with the key
    fernet = Fernet(key)

    # then use the Fernet class instance
    # to encrypt the string string must
    # be encoded to byte string before encryption

    encMessage = fernet.encrypt(password.encode())

    credentials[username] = {'key': key, 'encMessage': encMessage}
    print(credentials)


    print("encrypted string: ", encMessage)

    # decrypt the encrypted string with the
    # Fernet instance of the key,
    # that was used for encrypting the string
    # encoded byte string is returned by decrypt method,
    # so decode it to string with decode methods

    # decMessage = fernet.decrypt(encMessage).decode()
    # print(credentials)
    # print("decrypted string: ", decMessage)


def check_for_user(name, password, credentials):
    if name in credentials.keys():
        # hash the pass
        if password == name['pass']:
            ... # call the function
        else:
            print('Wrong password, try again')
    else:
        print('There is no such username registered')

