s = 'hello'
print(s[1]) # e

print(s[::-1]) # olleh

print(s[-1])
print(s[4])
try:
    s[len(s)]
except IndexError:
    print('IndexError')
finally:
    print('It always runs')