import math

number_items = int(input("\nEnter the number of items: "))
items_per_box = int(input("Enter the number of items per box: "))

number_boxes = math.ceil(number_items / items_per_box)

print(
    f"For {number_items} items, packing {items_per_box} items in each box, you will need {number_boxes} boxes.\n"
)
