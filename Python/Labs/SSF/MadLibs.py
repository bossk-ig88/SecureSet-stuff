import random

verbs_tup=("poop", "fornicate", "wiggle")
animals_tup=("space invaders", "wookie", "klingon")
people_tup=("Trump", "Clinton", "Bin Laden", "Jabba the Hut")
places_tup=("Eros", "Ceres", "a Super Massive Black Hole")
seasons_tup=("Winter", "Spring", "Mating Season", "Hunting Season")
superheroes_tup=("Batman", "Capt America", "Joker", "Thor")

verb = random.randint(0,len(verbs_tup)-1)
animal = random.randint(0,len(animals_tup)-1)
people = random.randint(0,len(people_tup)-1)
place = random.randint(0,len(places_tup)-1)
season = random.randint(0,len(seasons_tup)-1)
superhero = random.randint(0,len(superheroes_tup)-1)

print(elements[value])

print(text1 + text2)


print=Every <season>, <superhero> is joined by The <animal>, \
who’s secret identity is <people>. \
They attempt to <verb>, which rarely succeeds. \
So instead they chase down a villain in <places>.
