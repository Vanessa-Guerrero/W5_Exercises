# Question 5. You are going to tile a room whose dimensions are length by width feet. There are twelve tiles
            # per box, each 1 foot by 1 foot. How many boxes of tiles do you need?  
            # You can only buy full boxes, not a partial box.
            # You also want to buy 10% more tiles than you need in order to handle chips, breakage, & mess-ups.
            # How many total boxes will you buy?

import math

length = float(input("What is the length of the room in feet? "))
width = float(input("What is the width of the room in feet? "))
room_dimension = length*width
tiles_in_1_box = 12
tiles_needed = room_dimension + (room_dimension * .10)

total_boxes = math.ceil(tiles_needed / tiles_in_1_box)

print(f"I will need {total_boxes} boxes of tiles for the room")