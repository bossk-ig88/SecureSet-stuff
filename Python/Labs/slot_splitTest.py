# slot and split test
import math
# Math Definitions
def add(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def divide(num1, num2):
    return num1 / num2

# User input
userinput = input("Enter equation:")
print("CHECK 1. User input = ", userinput)

# FIND OPERATORS:
# Add
userslotAdd = userinput.find("+")
print("CHECK 1.i. Operator Slot =", userslotAdd)
# Subtract
userslotMinus = userinput.find("-")
print("CHECK 1.ii. Operator Slot =", userslotMinus)
# Multiply
userslotTimes = userinput.find("*")
print("CHECK 1.iii. Operator Slot =", userslotTimes)
# Divide
userslotDivide = userinput.find("/")
print("CHECK 1.iv. Operator Slot =", userslotDivide)

# if Add operator slot > 1, it splits string
if userslotAdd > 1:
    print("Start ADD math")
    userslotAdd = userinput.split()
    print("CHECK 2. Items in slot list:", userslotAdd)

    # for slot in the Add equation:
    for x in userslotAdd:
        print("CHECK 2.i. Start Add LOOP")
        # If x is Number 1 (slot 0), convert to integer:
        if x == userslotAdd[0]:
            num1 = int(x)
            print("CHECK 2.i.i Slot [0] =", x, ", convereted to integer =", num1)
        # If x is Operator (slot 1), create variable:
        elif x == userslotAdd[1]:
            operator = userslotAdd[1]
            print("CHECK 2.i.ii Slot [1] is Operator =", operator)

        # If x is Number 2 (slot 2), convert to integer:
        elif x == userslotAdd[2]:
            num2 = int(x)
            print("CHECK 2.i.iii. Slot [2] =", operator, ", convereted to integer =", num2)

    # Adding integers:
    print("CHECK 4. FINAL.",num1,"+",num2, "=", add(num1,num2))

# if Subtraction operator slot > 1, it splits string
elif userslotMinus > 1:
    print("Start SUBTRACTION")
    userslotMinus = userinput.split()
    print("CHECK 3. Items in slot list:", userslotMinus)

    # for slot in the Minus equation:
    for x in userslotMinus:
        print("CHECK 3.i. Start Minus LOOP")
        # If x is Number 1 (slot 0), convert to integer:
        if x == userslotMinus[0]:
            num1 = int(x)
            print("CHECK 3.i.i Slot [0] =", x, ", convereted to integer =", num1)
        # If x is Operator (slot 1), create variable:
        elif x == userslotMinus[1]:
            operator = userslotMinus[1]
            print("CHECK 3.i.ii Slot [1] is Operator =", operator)

        # If x is Number 2 (slot 2), convert to integer:
        elif x == userslotMinus[2]:
            num2 = int(x)
            print("CHECK 3.i.iii. Slot [2] =", x, ", convereted to integer =", num2)

    # Subtract integers:
    print("CHECK 5.FINAL.",num1,"-",num2, "=", subtract(num1,num2))

# if Multiply operator slot > 1, it splits string
elif userslotTimes > 1:
    print("Start MULTIPLICATION")
    userslotTimes = userinput.split()
    print("CHECK 4. Items in slot list:", userslotTimes)

    # for slot in the Multiply equation:
    for x in userslotTimes:
        print("CHECK 3.i. Start Minus LOOP")
        # If x is Number 1 (slot 0), convert to integer:
        if x == userslotTimes[0]:
            num1 = int(x)
            print("CHECK 3.i.i Slot [0] =", x, ", convereted to integer =", num1)
        # If x is Operator (slot 1), create variable:
        elif x == userslotTimes[1]:
            operator = userslotTimes[1]
            print("CHECK 3.i.ii Slot [1] is Operator =", operator)

        # If x is Number 2 (slot 2), convert to integer:
        elif x == userslotTimes[2]:
            num2 = int(x)
            print("CHECK 3.i.iii. Slot [2] =", x, ", convereted to integer =", num2)

    # Multiply integers:
    print("CHECK 6.FINAL.",num1,"*",num2, "=", multiply(num1,num2))

# if Divide operator slot > 1, it splits string
elif userslotDivide > 1:
    print("Start DIVISION")
    userslotDivide = userinput.split()
    print("CHECK 5. Items in slot list:", userslotDivide)

    # for slot in the Minus equation:
    for x in userslotDivide:
        print("CHECK 3.i. Start Minus LOOP")
        # If x is Number 1 (slot 0), convert to integer:
        if x == userslotDivide[0]:
            num1 = int(x)
            print("CHECK 3.i.i Slot [0] =", x, ", convereted to integer =", num1)
        # If x is Operator (slot 1), create variable:
        elif x == userslotDivide[1]:
            operator = userslotDivide[1]
            print("CHECK 3.i.ii Slot [1] is Operator =", operator)

        # If x is Number 2 (slot 2), convert to integer:
        elif x == userslotDivide[2]:
            num2 = int(x)
            print("CHECK 3.i.iii. Slot [2] =", x, ", convereted to integer =", num2)

    # Divide integers:
    print("CHECK 7.FINAL.",num1,"/",num2, "=", divide(num1,num2))

else:
    print("CHECK 6. PUNT!")

print("END OF LINE...")
