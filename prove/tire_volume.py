import math
from datetime import datetime
import sys

width = float(input("\nEnter the width of the tire in mm (ex 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"\nThe approximate volume is {volume:.2f} liters\n")

current_date = datetime.date(datetime.today())

with open("volumes.txt", mode="at") as file:
    print(current_date, round(width), round(aspect_ratio), round(diameter), round(volume, 2), sep=", ", end="\n", file=file, flush=False)