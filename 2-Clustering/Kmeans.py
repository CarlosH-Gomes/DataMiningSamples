import numpy as np
from scipy.spatial.distance import cdist
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import *
import matplotlib.pyplot as plt
import pandas as pd

# Defining our kmeans function from scratch


def KMeans_scratch(x, k, no_of_iterations):
    idx = np.random.choice(len(x), k, replace=False)
    # Randomly choosing Centroids
    centroids = x[idx, :]  # Step 1

    # finding the distance between centroids and all the data points
    distances = cdist(x, centroids, 'euclidean')  # Step 2

    # Centroid with the minimum Distance
    points = np.array([np.argmin(i) for i in distances])  # Step 3

    # Repeating the above steps for a defined number of iterations
    # Step 4
    for _ in range(no_of_iterations):
        centroids = []
        for idx in range(k):
            # Updating Centroids by taking mean of Cluster it belongs to
            temp_cent = x[points == idx].mean(axis=0)
            centroids.append(temp_cent)

        centroids = np.vstack(centroids)  # Updated Centroids

        distances = cdist(x, centroids, 'euclidean')
        points = np.array([np.argmin(i) for i in distances])

    return points


def show_digitsdataset(digits):
    fig = plt.figure(figsize=(6, 6))  # figure size in inches
    fig.subplots_adjust(left=0, right=1, bottom=0,
                        top=1, hspace=0.05, wspace=0.05)

    for i in range(64):
        ax = fig.add_subplot(8, 8, i + 1, xticks=[], yticks=[])
        ax.imshow(digits.images[i], cmap=plt.cm.binary,
                  interpolation='nearest')
        # label the image with the target value
        ax.text(0, 7, str(digits.target[i]))

    # fig.show()


def plot_samples(projected, labels, title):
    fig = plt.figure()
    u_labels = np.unique(labels)
    for i in u_labels:
        plt.scatter(projected[labels == i, 0], projected[labels == i, 1], label=i,
                    edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('tab10', 10))
    plt.xlabel('component 1')
    plt.ylabel('component 2')
    plt.legend()
    plt.title(title)


def main():

    k = 8
     # Faz a leitura do arquivo
    names =['date','quarter','department','day','team','targeted_productivity','smv','wip','over_time','incentive','idle_time','idle_men','no_of_style_change','no_of_workers','actual_productivity','productivity'] # Nome das colunas 
    features  = ['targeted_productivity','smv','over_time','actual_productivity'] # Define as colunas que serão  utilizadas
    input_file = '0-Datasets/garments_worker_productivityClear.data'
    target = 'productivity'
    df = pd.read_csv(input_file,    # Nome do arquivo com dados
                     names = names) # Nome das colunas                      


    # Separating out the features
    x = df.loc[:, features].values
    
    # Separating out the target
    y = df.loc[:,[target]].values
    
    # Standardizing the features
    x = MinMaxScaler().fit_transform(x)
    normalizedDf = pd.DataFrame(data = x, columns = features)
    normalizedDf = pd.concat([normalizedDf, df[[target]]], axis = 1)
   
    # PCA projection
    pca = PCA(2)
    projected = pca.fit_transform(x)
    print("Variância expleined por componente:")
    print(pca.explained_variance_ratio_)
    print(df.shape)
    print(projected.shape)
    print("")

    # Applying our kmeans function from scratch
    labels = KMeans_scratch(projected, k, 100)

    # Visualize the results
    plot_samples(projected, labels, 'Clusters Labels KMeans from scratch')

    # Applying sklearn kemans function
    kmeans = KMeans(n_clusters=k, random_state=0).fit(projected)
    print("inertia_ = ", kmeans.inertia_)
    silhouetteScore = silhouette_score(projected, kmeans.labels_)
    print("Para n_clusters = {}, silhouette_score é {})".format(
        k, silhouetteScore))

    # Visualize the results sklearn
    plot_samples(projected, kmeans.labels_,
                 'Clusters Labels KMeans from sklearn')

    plt.show()


if __name__ == "__main__":
    main()