###  SSF Lab 07 Python 2
##ADVANCED Lab
# Import random module
import random

userNum = int(input("Pick a number between 1 and 10: "))

# Computer choice list of numbers, between 1 and 10.
computerNum=random.randint(1,10)
print(computerNum)

# counts number of user attempts
count = 1

# Checks number from user when they don't equal other:
while userNum != computerNum:
    # user input for guess, between 1 and 10 (substring)
    # if user input < computer number:
    if count == 3:
        print("PUNT!!! Try again. " + str(count) + " attempts")
        break

    else:
        if userNum < computerNum:
            print('Too low Hoss!')
            # if count < 3:
            count +=1   # Increment counter
            print("Attempts left:", 4 - count)
            userNum = int(input("Pick again: "))

        # if user input > computer number:
        if userNum > computerNum:
            print('Too high Bub!')
            # if count < 3:
            count +=1   # Increment counter
            # print("Attempts left:", 3 - count)
            print("Attempts left:", 4 - count)
            userNum = int(input("Pick again: "))

# When answer is correct:
else:
    count += 1
    print("(User Guess) " + str(userNum) + " = " + str(computerNum) + " (Computer Input)")
    # display current count number:
    print("YES!!  Attempts = " + str(count))
