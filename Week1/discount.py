# import math
#
# people = [
#     "Stephanie 36",
#     "John 29",
#     "Emily 24",
#     "Gretchen 54",
#     "Noah 12",
#     "Penelope 32",
#     "Michael 2",
#     "Jacob 10"
# ]
# youngest = math.inf
# for people in people :
#     items = people.split()
#     if youngest > float(items[1]):
#         youngest = int(items[1])
#     print(items)
# print(youngest)
city_name = "Accra"
elevation = 61
population = 4200000
# Open a text file named cities.txt in append mode.
with open("cities.txt", "at") as cities_file:
  # Print a city's name and information to the file.
  print(city_name, file=cities_file)
  print(f"{elevation}, {population}", file=cities_file)