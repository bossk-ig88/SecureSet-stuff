import random

choices=("Stay classy", "Loud Noises!", \
"I have a headache", "Cannot predict now", "Great story...compelling and rich", \
"Ask again later", "Yes", "No", "Thanks for stopping by", \
"James Westfall", "Dr Kenneth Noisewater")

value = random.randint(0,len(choices)-1)
print(choices[value])
