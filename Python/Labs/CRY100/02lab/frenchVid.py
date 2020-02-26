#!/usr/bin/python3

plaintext = ("have a nice day")


key = 14

ciphertext = [''] * key
print(ciphertext)
print(len(plaintext))

for column in range(key):
    pointer = column

    while pointer < len(plaintext):
        ciphertext[column] += plaintext[pointer]
        #print(ciphertext)

        pointer += key

print(''.join(ciphertext))
