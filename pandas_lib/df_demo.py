import numpy as np
import pandas as pd

# Index Levels
outsidees = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outsidees, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
df = pd.DataFrame(np.random.randn(6, 2), hier_index, ['A', 'B'])
print(df)