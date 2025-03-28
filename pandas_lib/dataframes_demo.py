import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101) 

df = pd.DataFrame(randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df['X'])
print(type(df['W']))
print(type(df))
print(df[df > 0])

print(df[df['Z'] < 0])