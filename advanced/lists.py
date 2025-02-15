# https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
l = [1,2,1,3]
l.append(4)
# print(l.count(1))

l1 = [1,2,3]
l2 = [4,5]
l1.append(l2) # [1, 2, 3, [4, 5]]
print(l1)  # [1, 2, 3, [4, 5]]
# reassign
l1 = [1,2,3]
l2 = [4,5]
l1.extend(l2) # [1, 2, 3, 4, 5]
print(l1) # [1, 2, 3, 4, 5]

# occurs exception
try:
    l1.index(33)
except ValueError as ve:
    print(f'Index {ve}')
    
    
my_list = [1,2,3]
my_list.insert(1,'Prashanth Sagari')
print(my_list)

print(my_list.pop())
print(my_list)

print(my_list.pop(0))
print(my_list)