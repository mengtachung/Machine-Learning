from pandas import DataFrame
#import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

Data = {'x': [1, 1, 0, 2, 3],
        'y': [1, 0, 2, 4, 5]
       }
  
df = DataFrame(Data,columns=['x','y'])
  
kmeans = KMeans(n_clusters=2).fit(df)
centroids = kmeans.cluster_centers_
labels = kmeans.labels_
print(centroids)
print(labels)

#plt.scatter(df['x'], df['y'], c= kmeans.labels_.astype(float), s=50, alpha=0.5)
#plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
