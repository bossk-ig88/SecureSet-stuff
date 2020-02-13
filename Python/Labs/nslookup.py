#SYS 100 - Python - nslookup and curl
# Determine vailidity and certificate authority of a website
# Will ask user for a URL to check if the SSL cert matches the URL and is valid.

# 1. Input function
# 2. Use Requests.verify(ssl certificate)
# 3. Open SSL to get cert check alt name
# if number 2 and number 3 == True:
#     GTG
# else:
#     NoGo
# 1. Input function
import requests

# 2. Get user input of what URL to check
URL = input("What website checking? \n")

# 3. check if SSL cert for the request website is valid usig the requests module.
try:
    info = requests.get("https://"+URL)
    if(info.ok == True):
        print('Safe Site')
except requests.exceptions.SSLError:
    print("Unsafe Site")
except requests.exception.ConnectionError:
    print("Cannot find URL")
