# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
# print("The total due is " + str(total_due))

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
# print("Tip is "  + str(tip))
print("Total due is " + str(total_due))

print("Tip is " + format(tip, ".2f")) # .2f defines the number of decimals (default is 6), so period, number of decimals, and f for fixed point number
