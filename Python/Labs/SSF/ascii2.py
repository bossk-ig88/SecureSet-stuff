lowercase = []     # List 1
uppercase = []     # List 2

for num in range(65,91):
    c1 = chr(num)              # convert to ASCII
    ordinal = ord(c1)           # get ordinal value
    # have ASCII character and value in pairs inside of lowercase list.
    lowercase.append(c1)
    lowercase.append(ordinal)

for num in range(97,123):
    c2 = chr(num)              # convert to ASCII
    ordinal = ord(c2)           # get ordinal value
    # have ASCII character and value in pairs inside of lowercase list.
    uppercase.append(c2)
    uppercase.append(ordinal)

LU = 0
LU2 = 1

for item in range(0,26):
    print(lowercase[LU], str(lowercase[LU2]), \
    uppercase[LU], str(uppercase[LU2]))
    LU += 2
    LU2 += 2
