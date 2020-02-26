##  SSF Lab 07 Python 2
#
# usertext = input("What word would you like to convert? ")
# for let in usertext:
#     print(ord(let))

letters = {}    # Dictionary with a letter paired with the number of times letter typed.

userword = input("What word or phrase do you want to analyze? ").upper() # converts the user input to upper case

#For letter in user's words
for lett in userword:
     #Checks if that letter is in dictionary exists or not.  If it doesn't exist:
    if lett in letters.keys():
        # Adds a value of 1 (increase of occurance of letter by user)
        # for that letter and assigns that new value to that key location in dictionary
        letters[lett] += 1

        # If letter exists in dictionary already, value remains at 1 (unchanged):
    else:
        letters[lett]=1

# for key with letter and its corresponding value in the Letters dictionary,
# returns a new view of the dictionary's items ((key, value) pairs)
for key, value in letters.items():
    # displays key (user's letter...string)  "occurs" for numerical value
    # (number of "times", converted to string from integer) the letter was input
    print (key + " occurs " + str(value) + " times")

print(letters)
