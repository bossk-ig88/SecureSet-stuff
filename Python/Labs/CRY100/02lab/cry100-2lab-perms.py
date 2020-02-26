#!/usr/bin/python3
# CRY 100-2 Lab - Permutation Cipher
# 1. Write a function that will alphabetize a string of characters.
indexList = []  # List of Index Values or sorted letters.
myword = "Have a nice day"

# Sort string into alphabetical order:
oldword=sorted(myword)
# 2. Create a list from the indices for each letter in sorted string:
for lett in oldword:
    # take the alphabetized string and create a list from the indices.
    myword.replace(lett,'.',1)

# Index sorted letters:
for x in range(len(oldword)):
    # Index values for sorted letters.
    index = print("Index:",x, "=", end = " ")
    #Sorted Letters
    print(oldword[x])
    # Create list of Index values:
    indexList.append(x)

print("Index List:",indexList)

# 3. Use "indexList" to parse down through the "myword" and rearrange the
#    letters in each block based on the position in the new index list.
# (easy) Just rearrange the letters in each block, with the size of the block equal to the key.
