# Question 6. There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost 
            # $250 per day to rent (including the driver’s pay). How many vans do you need? 
            # How much will it cost to rent vans? What is the cost if you split it per person?

import math

people = int(input("How many people are going on a tour? "))
seats = 15

vans = math.ceil(people / seats)

total_cost = 250 * vans

cost_split_people = round((total_cost / people), 2)

money_collected = round((cost_split_people * people), 2)

print(f"The tour had {people} guests. I needed {vans} vans to seat all the guests.")
print(f"The 3 vans cost ${total_cost} to rent for the day. I charged ${cost_split_people} per guest to cover the cost.") 
print(f"I collected in total ${money_collected}. I had some leftover money since I rounded up the decimal.")




 