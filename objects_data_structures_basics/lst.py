list1 = [0] * 3
print(list1)

list2 = [0 for i in range(10)]
print(list2)

list3 = (i for i in range(10))  #  generator
print(next(list3))
print(next(list3))
print(next(list3))
print(next(list3))
print(next(list3))

list4 = [1,2,[3,4,'hello']]
list4[2][2] = 'goodbye'
print(list4)


list5 = [5,3,4,6,1]
list5.sort()
print(list5)
list5.sort(reverse=True)
print(list5)
list6 = ['Prashanth']
print(list6)
list6.append('Kumar')
print(list6)