# Define known values
assets = 1500
debts = 450.50

# Calculate the unknown
net_worth = assets - debts

# Display the results
print("Your net worth is " + str(net_worth))  # without commas

print("Your net worth is " + ('{:,.2f}'.format(net_worth))) # with commas and 2 decimal place