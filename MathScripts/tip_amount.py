# Question 3. How do you calculate the tip amount on a restaurant bill given the tip percentage?

# Define known values
food_cost = 55
tip_perc = float(input("How much would you like to give tip in percentage? "))      # Bonus 1

# Calculate the unknown
tip_amount = food_cost * (tip_perc/100)

# Display the results
print("The tip on a $" + str(food_cost) + " restaurant bill is $" + ('{:.2f}'.format(tip_amount)))