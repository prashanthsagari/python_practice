from InvalidRangeException import InvalidRangeException

def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)

row1 = ['','','']
row2 = ['','','']
row3 = ['','','']
row2[1] = 'X'
display(row1,row2, row3)
position_index = 0

try:
   position_index = int(input("Choose an index position : "))
   if position_index not in range(0,3):
       raise InvalidRangeException("Only 0, 1, 2 are allowed.")
except InvalidRangeException as ire:
    print(ire)
except ValueError as e:
    print(f'Only Integer is allowed {e}')

