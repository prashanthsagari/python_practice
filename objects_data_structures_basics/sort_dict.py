data = {'b': 2, 'a': 5, 'c': 1}

print(data.keys()) 
print(data.values())
print(data.items())

print(dict(sorted(data.items())))
print(dict(sorted(data.items(), reverse=True)))
