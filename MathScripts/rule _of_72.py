# Question 5. How long will it take a savings account worth X to double in value based on an interest rate of IR? (Hint: Look up the rule of 72)?



interest_rate = .08
current_savings_acct = 15000

rule_of_72 = 72 / (interest_rate*100) # rule to find how many years it would take to approx double you amount
years = rule_of_72 # 8 years

future_savings_account = current_savings_acct*(1+interest_rate)**years # future savings account balance

print ("At a " + format(interest_rate, ".0%") + " interest rate, your savings account will be worth " + ("{:,.2f}".format(future_savings_account)) + " in " + format(years, ".1f") + " years")
