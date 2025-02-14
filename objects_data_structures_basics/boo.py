print(2 > 3) # False
print(3 <= 2) # False
print(3 == 2) # False
print(3.0 == 3) # True
print(4**0.5 != 2) # False

# two nested lists
l_one = [1,2,[3,4]]
l_two = [1,2,{'k1':4}]

# True or False?
# 3 >= 4
print(l_one[2][0] >= l_two[2]['k1']) # False