from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


scaler = StandardScaler()
dataframe = pd.read_csv('dataframe_filtrado.csv')
x = dataframe[['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9']].values
y = dataframe["RP"].values
scaler.fit(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.7, random_state=21, stratify=y)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)
train_accuracies = {}
test_accuracies = {}
neighbors = np.arange(1,24)


for neighbor in neighbors:
    knn = KNeighborsClassifier(n_neighbors=neighbor)
    knn.fit(x_train,y_train)
    train_accuracies[neighbor] = knn.score(x_train, y_train)
    test_accuracies[neighbor] = knn.score(x_test, y_test)

plt.figure(figsize=(8,6))
plt.title("Acurácia do modelo de classifação do knn, para n possíveis valores para k")
plt.plot(neighbors, train_accuracies.values(), label="Training accuracies")
plt.plot(neighbors, test_accuracies.values(), label="Testing accuracies")
plt.legend()
plt.xlabel("Kneighbors")
plt.ylabel("Accuracies")
plt.show()





