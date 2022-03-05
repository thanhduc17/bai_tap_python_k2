import numpy as np
import pandas as pd

s = pd.Series()
print(s)
data = np.array(['a', 'b', 'c', 'd'])
s = pd.Series(data, index=[100, 101, 102, 103])
print(s)
