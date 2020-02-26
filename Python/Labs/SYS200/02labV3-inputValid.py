#!/usr/bin/python3
# SYS 200 - 02 LAB - Input Validation
# vi 2
blacklist = ["BabaYaga", "johnwick"]

whitelist = ["rob", "Rob"]

#
name = input("Enter your Username: ")

if name == whitelist:
    print("Hello", name)

    pwd = input("Enter Password: ")

    if pwd == "asdf":
        print("Access Granted...Accessing Archived Data.")
    else:
        print("Password incorrect.  Try again.")


elif name == blacklist:
    print("Hello, {name}, You're on the Black List.")

else:
    print("UserID incorrect. Try again.")






##if name == "Rob" or name == "rob":
##
##    print("Hello", name)
##    pwd = input("Enter Password: ")
##    if pwd == "asdf":
##        print("Access Granted...Accessing Archived Data.")
##    else:
##        print("Password incorrect.  Try again.")
##        
##if name == "tls" or name == "TLS":
##    print("You're on the Black List, fuck off.")



