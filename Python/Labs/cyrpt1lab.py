alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# 1. Get message.  User input: string or integers
userwords = input("Text to encrypt or decrypt:  ")
userwords = ""

# 2. Get a rotation integer from user.
rotate = input("Rotation Parameter:  ")
rotate = int()

# 4. If encrypt:

question = ("e","d")
print(question)
# loop check...when user response is NOT encrypt)
while (question != "e"):
    # 3. Ask user if want to encrypt or decrypt
    question = input("Want 'Encrypt' or 'Decrpyt'?  Use 'e' for encrypt, and 'd' for decrpyt:  ")
    if (question == "e"):
        # 4.a) index user input message
        for letter in userwords:
            # Index and add user rotate input
            newletter = (alphabet.index(letter) + rotate)%26
            # Match user letter to alphabet
            indexRotatednewletter = (alphabet.index(newletter))
            print(indexRotatednewletter)


    # 5. If decrypt:
    else:
        # 5. a) Index and remove Rotation
        for letter in userwords:
            oldletter = (alphabet.index(letter) - rotate)%26


# Print  user input as encrypted
print("Your ", userwords, " are now encrypted as:  ",  indexRotatednewletter)
