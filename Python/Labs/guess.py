# use if-else statement
# Evaluate/result to True or false (boolean)
# use == to determine if 2 things are equal.

# add 2 tuple variables: 1 for correct guess, 1 for incorrect guess.
# only add 2 variables
# only change the 2 print statements
# Have output be a random selection from the tuples

import random

userguess = int(input("Pick a number between 1 and 10: "))

# Tuples with correct guess:
pos = ("YES! Now that squirrel can water ski!", \
"YES! When in Rome!")
posrandom = random.randint(0,len(pos)-1)

# Tuples with wrong guess:
neg = ("NO! Diversity is an old old wooden ship used in the Civil War era", \
"NO! Discovered by the Germans in 1904.")
negrandom = random.randint(0,len(neg)-1)

myguess = random.randint(1,10)

print("Is your number " + str(myguess) + "?")

if(myguess == userguess):
    print(pos[posrandom])
else:
    print(neg[negrandom])
