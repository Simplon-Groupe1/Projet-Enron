import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
from sklearn.cluster import KMeans

#from sklearn.datasets.samples_generator import make_blobs
import sample.csv[6] as sample

X, y_true = sample
plt.scatter(X[:, 0], X[:, 1], s = 50);
#On affiche l'échantillon de base pour avoir une idée du nbr de clusters
plt.show()

#On choisit le nombre de clusters à effectuer
kmeans = KMeans(n_clusters = 4)

#Création entraînement
kmeans.fit(X)
y_kmeans = kmeans.predict(X)
plt.scatter(X[:, 0], X[:, 1], c = y_kmeans, s = 50, cmap = 'viridis')

centers = kmeans.cluster_centers_

#création du graph
plt.scatter(centers[:, 0], centers[:, 1], c = 'black', s = 200, alpha = 0.5);
plt.show()