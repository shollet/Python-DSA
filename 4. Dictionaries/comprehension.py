import random

cityNames = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']

cityTemps = {city: random.randint(20,30) for city in cityNames}
print(cityTemps)
above_25 = {city: temp for (city,temp) in cityTemps.items() if temp > 25}
print(above_25)