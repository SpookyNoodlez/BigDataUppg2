import pandas as pd
import numpy as np


rng = np.random.RandomState(np.random.seed())
ser = pd.Series(rng.randint(0, 10, 4))

A = pd.DataFrame(rng.randint(0, 20, (8, 10)),
                 columns=list('ABCDEFGHIJ'))


B = A.loc[:, 'C'] - A.loc[:, 'C']


print(B)

#Jag förstår inte riktigt frågan. Är det det här du ville ha?