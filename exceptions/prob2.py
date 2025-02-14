x = 5
y = 0
try:
    print(x/y)
except ZeroDivisionError as zde:
    print(f'Error {zde}')