import numpy as np
import pandas as pd

arr = np.array([1,2,3,4,5])
labels = ['a', 'b', 'c', 'd', 'e']
nparr = np.arange(1, 6)
dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# s = pd.Series(arr)
s = pd.Series(arr,labels)
print(s)

a = pd.Series(nparr, labels)
print(a)


d = pd.Series(dict)
print(f"{d} \n Dictionary")

