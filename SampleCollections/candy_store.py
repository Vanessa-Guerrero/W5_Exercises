# Defining my candies and fruit flavors
candy_types = ('Lollipops', 'Gummy Bears', 'Jelly Beans')
fruity_flavors = ('Apple', 'Blue Raspberry', 'Orange')

# Defining my candy_combos varaible as an empty set
candy_combos = set()

# Adding candy combos 
candy_combos.add((fruity_flavors[0], candy_types[0]))   # Apple Lollipops
candy_combos.add((fruity_flavors[1], candy_types[0]))   # Blue Raspberry Lollipops
candy_combos.add((fruity_flavors[2], candy_types[0]))   # Orange Lollipops
candy_combos.add((fruity_flavors[0], candy_types[1]))   # Apple Gummy Bears
candy_combos.add((fruity_flavors[1], candy_types[1]))   # Blue Raspberry Gummy Bears
candy_combos.add((fruity_flavors[2], candy_types[1]))   # Orange Gummy Bears
candy_combos.add((fruity_flavors[0], candy_types[2]))   # Apple Jelly Beans
candy_combos.add((fruity_flavors[1], candy_types[2]))   # Blue Raspberry Jelly Beans
candy_combos.add((fruity_flavors[2], candy_types[2]))   # Orange Jelly Beans

print(f"Today's candy options include: {candy_combos}") # prints it in a different order with each output