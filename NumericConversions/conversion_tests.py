# Description: This script tests various numeric 
#              conversion techniques
# Author: Vanessa G. Newprogrammer 

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 ' 

# Testing variable 'a' for the following transformations:

# a1 = int(a)
# print(a1, type(a1))    # error: invalid literal for int() with base 10: ' 101.1 '

a2 = float(a)
print(a2, type(a2))

a3 = int(float(a))
print(a3, type(a3))

a4 = str(a[1:6])
print(a4, type(a4))

a5 = a.strip()
print(a5, type(a5))         # a4 and a5 produced same result

# Testing variable 'b' for the following transformations:

b1 = int(b)
print(b1, type(b1))  

b2 = float(b)
print(b2, type(b2))

b3 = int(b[0:])
print(b3, type(b3))

# Testing variable 'c' for the following transformations:

# c1 = int(c)
# print(c1, type(c1))       # error: invalid literal for int() with base 10: '402 Stevens'

# c2 = float(c)
# print(c2, type(c2))       # error: could not convert string to float: '402 Stevens'

c3 = int(c[0:3])
print(c3, type(c3))

# Testing variable 'd' for the following transformations:

# d1 = int(d)
# print(d1, type(d1))       # error: invalid literal for int() with base 10: 'Number 5 '

# d2 = float(d)
# print(d2, type(d2))       # error: could not convert string to float: 'Number 5 '

d3 = int(d[7])
print(d3, type(d3))

d4 = d.strip()
print(d4, type(d4))



