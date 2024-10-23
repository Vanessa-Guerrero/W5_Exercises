# Question 3. Federal taxes are 23% of your salary every month. You make X amount of money. 
 # How much is withheld for taxes?

salary = int(input('What is your monthly gross salary? $'))

taxes = (salary * .23)

print(f"The amount of taxes withheld from your monthly salary is $ {taxes:,.2f}")
