# https://docs.python.org/3/tutorial/datastructures.html#sets
s = set()
s.add(1)

s.add(2)
s.add(2)
print(f'Before clearing data in sets {s}')
s.clear()
print(f'After clearing data in sets {s}')
s = {1,2,3}
sc = s.copy()
print(sc)
sc.add(5)

print(sc)

print(s)

print(sc.difference(s))

