# # SSF100 Python Lab 8a
#
# # Base Lab
# # FUNCTIONS
#
#
import math

# Area of Circle
def area_of_circle(rad):
    return round(math.pi * rad**2,2)

# circumference_of_circle
def circumference_of_circle(rad):
    return round(math.pi * 2 * rad,2)

# Allows python to check if this is the Primary Script (Main) \
# or if this is being called by an import statement.
# If imported, then the main function wil not be executed.
# This will allow the functions to be used in the calling script.
if __name__ == '__main__':
    radius = int(input("What is the radius? "))
    print("The area is", area_of_circle(radius))
    print("The circumference is", circumference_of_circle(radius))

# madlibs from first Lab
# import random module
import random

# Tuple variables.
noun=("car","bus","ball","plane","cup")
verb=("jump","sit","run","think","smile")
superhero=("Superman","Wonder Woman","Batgirl","Batman")
animal=("dog","cat","octopus","wolverine","snail","monkey")
people=("Abe","Jim","Gary","Michelle","Kimberly","Megan","Omar")
places=("the Citadel Mall","Denver","North Pole","downtown")
season=("spring","winter","fall","summer")

# elem function. Generates pseudo-random numbers.
# random.randint(a,b)
# Returns a random integer N, such that a <= N <= b.  Alias for randrange(a, b+1)
# len() function returns the length (number of items) of an object.
# Arguement may be a sequence (string, btes, tuple, list, or range) or
# a collection (such as a dictionary, set, or frozen set.)
def elem(tuple):
    value = random.randint(0,len(tuple)-1)
    return tuple[value]

# Allows the function to exist both as an independent script and also
# be called as an import and allows the reuse of the functions without running the code.
if __name__ == '__main__':
    print("Every " + elem(season) + ", " + elem(superhero) + \
    " is joined by The " + elem(animal) + \
    ", who's secret identity is " + elem(people) + \
    ". They attempt to " + elem(verb) +\
    ", which rarely succeeds. So instead they chase down a " + \
    "villain in " + elem(places) + " who was trying to steal a " + \
    elem(noun) + ".")

# Repetitive task for bool function
# Returns a Boolean value, one of True or False.
# bool([x])
# If x is false or omitted, this returns False; otherwise it returns True.
# Cannot be subclassed further. Only instances are: True and False.
def bool (a,b):
    return (a == b)

if __name__ == '__main__':
    val_a = input("What is the first value? ")
    val_b = input("What is the second value? ")

    print(bool(val_a,val_b))
