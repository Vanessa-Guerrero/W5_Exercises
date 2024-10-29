# dict1 = {
#     'orderID' : 1234,
#     'prod_name' : 'overalls',
#     'customerID' : 'BILBO',
#     'qty' : 4,
#     'price' : 79.99 
# }

# dict2 = {
#     'orderID' : 6789,
#     'prod_name' : 'staff',
#     'customerID' : 'GANDD',
#     'qty' : 1,
#     'price' : 159.99
# }

# dict1.update({'discount':.15})
# dict2.pop('orderID')
# dict2.popitem()

# print(dict2) 

# if [expression]:
#     result



#Define the known

# pumpkins = int(input("How many pumplins ya' got? (Whole numbers only): ")) # optimal pumpkin inventory = 1500

# p_ship = 400

# #Calculate the unknown
# if pumpkins < 600:
#     print(f"Pumpkin emergency! Only {pumpkins} pumpkins left")
#     pumpkins = pumpkins + (2 * p_ship)
#     print("Pumpkins ordered")
# elif pumpkins < 1200:
#     print(f"Time to order some pumpkins. {pumpkins} pumpkins left")
#     pumpkins += p_ship
#     print("Pumpkins ordered")
# elif pumpkins == 1500:
#     print(f"Woah! Exactly 1500 pumpkins")
# else: print("No order needed")

# # Display the results
# print (f"Now we have {pumpkins} pumpkins")

# apples = -800

# if apples != 0:
#     print("Yeah, we got apples")

##### START OF 10/28/24 #####

# sched1 = "Garbage pickup is Wednesday"
# sched2 = "Recycling pickup is Wednesday"
# sched3 = "Yard waste pickup is Friday"

# # print(sched1.find("Garbage"))
# # print(sched1.find("pickup"))
# # print(sched1.lfind("Wednesday"))

# print(f'''Schedule change! This week due to holiday:
#       {sched1.replace("Wednesday", "Thursday")}
#       {sched2.replace("Wednesday", "Thursday")}
#       {sched3.replace("Friday", "Monday")}''')


# inv_gar = 26
# inv_rec = 8
# inv_yw = 14

# total_bill = "Your total waste management bill is: {total:.2f}"

# # print(f'''Your total waste management bill is 
#     #   ${format(inv_gar + inv_rec + inv_yw, ".2f")}''')

# print(total_bill.format(total = inv_gar + inv_rec + inv_yw))


### Lesson 1.B ###

# import numpy as np
# import math 
# import statistics as stat

# gar_bill = [1.33, 4, 14.95]

# print(f'Total garbage bill is: $ {math.fsum(gar_bill)}')
# print(f'Avg line item amount: $ {stat.mean(gar_bill)}')
# print(f'Median line item amount: $ {stat.median(gar_bill)}')
# print(f'Bill sorted by amount: $ {sorted(gar_bill)}')

# import random

# print(random.random())

# print(random.randint(0,24))

# print(random.choices(gar_bill, k=10))

# import datetime

# print(datetime.datetime.now())

# def my_first_function():
#     return "Hello world!"

# print(my_first_function())

# def calc(n1, n2):
#     return n1 + n2

# print(calc(5, 96)) # adding comma cause return is adding

# def calc(n1, n2, operation):
#     print(f"Input values are {n1} and {n2}")
#     print(f"You have chosen the {operation} operation")
#     if operation == 'minus':
#      return n1 -n2
#     elif operation == 'times':
#      return n1 * n2
#     elif operation == 'divide':
#      return n1 / n2
#     else:
#      return n1 + n2

# print(calc(5, 96, 'plus'))

# def goodmorning(name, day_name='day'):
#     print('Good morning, ' + name + '! Have a good ' 
#     + day_name + '!')
# print(goodmorning('Dave', 'Tuesday')) # returning none because I'm not specifying a return value
# another way around this is instead of print the function, you can call it w/o print()
# like this: goodmorning('Dave', 'Tuesday')

