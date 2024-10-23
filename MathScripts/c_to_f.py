# Question 2. How do you convert a temperature from Celsius to Farenheit?

celsius = int(input('What is the temperature in Celsius? '))

farenheit = round((9/5) * celsius + 32)

print('The temperature converted to Farenheit is ' + str(farenheit))