import math

manufactured_items = int(input('Enter number of manufactured items: '))
items_per_box = int(input('Enter number of items per box: '))

# boxes_required = math.ceil(manufactured_items/items_per_box)
print(f"For {manufactured_items}, packing {items_per_box} in each box, you will need {math.ceil(manufactured_items/items_per_box)}")
