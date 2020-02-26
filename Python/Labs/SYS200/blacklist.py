#!/usr/bin/python3
# SYS 200 - 02 LAB - Input Validation
# white and black lists for UserIDs.

blacklist = ["babayaga", "johnwick"]
whitelist = ["Rob", "rob"]
name = input("Enter your Username: ")


for black in blacklist:
    if name in blacklist:
        print(f"Leave, {name}, you're banned.")
    break


for white in whitelist:
    if name in whitelist:
        if name == white:
            print("Hello", name)

            pwd = input("Enter Password: ")

            if pwd == "asdf":
                print("Access Granted...Accessing Archived Data.")
            
        
            else:
                print("Password incorrect.  Try again.")


    else:
        print("UserID incorrect. Try again.")
        break


