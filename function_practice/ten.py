
def up_low(s):
    lowercase = 0
    uppercase = 0
    
    for char in s:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        else:
            pass
    print(f'Lower case {lowercase}')
    print(f'Upper case {uppercase}')
    
up_low('Hello prAshanth')
