#!/usr/bin/python3

# It can be any transposition cipher the idea is to learn how
# to make a list of list and populate it with the text your going to encrypt

# ENCRYPT:
myword = "Have a nice day"
#myword = input("Enter Plain Text: ").upper()

keyList = []  # List of Index Values or sorted letters.

plaintext=sorted(myword)
for lett in plaintext:
    myword.replace(lett,'.',1)

# Index sorted letters:
for x in range(len(plaintext)):
    #index = print("Index:",x, "=", end = " ")
    #print(plaintext[x])
    keyList.append(x)

print("1. Index Key List:",keyList)

# Experiment block
lengthofkeylist = int(len(keyList))
print("2. Key length:", lengthofkeylist)

print("3. Sorted Text:", plaintext)

# Looping keys (number of columns) in Key List, create ciphertext:
for key in keyList:
    # ciphertext multiplied by enumarated keys from keylist:
    #print("2. Current Key in loop:", key)
    ciphertext = [''] * key
    #print("2.i. Ciphertext:", ciphertext)

    # for Cipher text columns in the range of keys:
    for column in range(key):
        pointer = column
        #print("3. Column:", column)
        #print("3.i. Pointer:", pointer)

        # If pointer is less than length of plaintext string:
        while pointer < len(plaintext):
            
            ciphertext[column] += plaintext[pointer]
            #print("4. Ciphertext:", ciphertext)

            pointer += key

print(''.join(ciphertext))
