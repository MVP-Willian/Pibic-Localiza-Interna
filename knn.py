import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

path = "./dataframe_filtrado.csv"

st = StandardScaler()
df = pd.read_csv(path)
x = df.loc[all,9]
print(x)