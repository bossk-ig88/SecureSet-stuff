classlist=[]

userclass = ""

while (userclass != "Done"):
    userclass = input("What classes do you like (Type 'Done' or 'done' when done)? ")
    if (userclass == "Done"):
        userclass.lower()
        break
    if (userclass == "done"):
        userclass.upper()
        break
    else:
        classlist.append(userclass)

print("You like the following classes:",classlist)

for cl in classlist:
    print(cl)
