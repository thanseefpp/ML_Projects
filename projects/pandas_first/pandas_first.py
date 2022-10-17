import pandas as pd
import numpy as np
data = pd.read_csv("datas.csv")

x = np.array(data['x1'])
y = np.array(data['y'])
print(x)