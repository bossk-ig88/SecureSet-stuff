# Split Test - accomodates spaces...uses them as deliminitors.
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
userinput = " 4 + 2 "
print("CHECK 1. User input = ", userinput)

# FIND OPERATORS:
slot = userinput.find("+")
print("CHECK 1.i. Operator Slot =", slot)

# if operator slot > 1, it splits string
if slot > 1:
    slot = userinput.split()
    print("CHECK 2. Items in slot list:", slot)

    # print(splitadd[0])
    for x in slot:
        print("CHECK 3. Start LOOP")
        # If x is Number 1 (slot 0), convert to integer:
        if x == slot[0]:
            num1 = int(x)
            print("CHECK 3.i. Slot 0 =", x, ", convereted to integer =", num1)
        # If x is Operator (slot 1), create variable:
        elif x == slot[1]:
            operator = slot[1]
            print("CHECK 3.ii. Slot 1 is Operator =", operator)

        # If x is Number 2 (slot 2), convert to integer:
        elif x == slot[2]:
            num2 = int(x)
            print("CHECK 3.iii. Slot 2 =", x, ", convereted to integer =", num2)

    # For Add Operator, if Slot 1 = "+":
    if operator == "+":
        # Adding integers:
        print("CHECK 4. FINAL.",num1,"+",num2, "=", add(num1,num2))

    # For Subtract Operator, if Slot 1 = "-":
    elif operator == "-":
        # Subtract integers:
        print("CHECK 5.FINAL.",num1,"-",num2, "=", subtract(num1,num2))

    # For Multiply Operator, if Slot 1 = "*":
    elif operator == "*":
        # Multiply integers:
        print("CHECK 6.FINAL.",num1,"*",num2, "=", multiply(num1,num2))

    # For Divide Operator, if Slot 1 = "/":
    elif operator == "/":
        # Divide integers:
        print("CHECK 7.FINAL.",num1,"/",num2, "=", divide(num1,num2))

    else:
        print("8. PUNT!!! Input invalid")
