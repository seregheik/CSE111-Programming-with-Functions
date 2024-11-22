import math
from datetime import datetime
width = int(input('Enter the width of the tire: '))
aspect_ratio = int(input('Enter the aspect ratio of the tire: '))
diameter = int(input('Enter the diameter of the tire: '))
volume = f"{((math.pi * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000):.2f}"
print(f'The Approximate volume is {volume} litres')

# ----BEGINNING OF CREATIVITY(not actually creative tho)----
# AVERAGE COST OF TIRES
# 12 - 15 inches cost roughly $80 to $150
# 16 - 20 inches cost roughly $100 to $400
# 18 - 26 inches cost about $400 to $500
# PS: dont take this pricing seriously
wheel_diameter = ((width * aspect_ratio)/(2540*2) + diameter)
base_price = 0
if (diameter >= 12) and (diameter <= 15) :
    base_price = 80
elif (diameter >= 16) and (diameter <= 20) :
    base_price = 100
elif (diameter >= 21) and (diameter <= 26):
    base_price = 400
estimated_price = F"{(wheel_diameter * 2 + base_price):.0F}"
print(f'The estimated cost of the tire would be about ${estimated_price}')
# ----END OF EXCEEDING ASSIGNMENT----

with open('volumes.txt', mode= 'at') as volumes_file :
    print(f"{datetime.now():%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume}, {estimated_price}", file=volumes_file)
