# print(i ** 2)
try:
    for i in ['a']:
        print(i ** 2)
except TypeError as e:
    print(f'Only numbers allowed')
else: 
    print('Skipping try')
