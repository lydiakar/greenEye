from sklearn.cluster import KMeans
import matplotlib
import matplotlib.pyplot as plt
from keras.datasets import mnist
import numpy as np
import random
from io import BytesIO
import base64


matplotlib.use('Agg')


# TODO(?): Add docstring to all methods

def generate_response(centroids, reference_labels, k, clusters, x_train):
    response = []
    # image plot characters
    plt.figure(figsize=(3, 3))
    plt.axis('off')
    # for every cluster - create image for the centroid
    for i in range(k):
        clusters_object = {'name': str(i), 'label': str(reference_labels[i])}
        img_center_plot = plt.imshow(centroids[i])
        with BytesIO() as img_buffer:
            img_center_plot.figure.savefig(img_buffer, format="png")
            img_buffer.seek(0)
            clusters_object['centred'] = base64.b64encode(img_buffer.read()).decode('utf-8')

        cluster_member_indices = np.where(clusters == i)[0]
        # create 5 random images from the cluster
        for j in range(5):
            random_member = random.choice(cluster_member_indices)
            img_plot = plt.imshow(x_train[random_member, :, :])
            with BytesIO() as img_buffer:
                img_plot.figure.savefig(img_buffer, format="png")
                img_buffer.seek(0)
                clusters_object['img_from_cluster_' + str(j)] = base64.b64encode(img_buffer.read()).decode('utf-8')
        response.append(clusters_object)
    return response


def retrieve_image_info(cluster_labels, y_train):
    reference_labels = {}
    # get real label of cluster label
    for i in range(len(np.unique(cluster_labels))):
        index = np.where(cluster_labels == i, 1, 0)
        number = np.bincount(y_train[index == 1]).argmax()
        reference_labels[i] = number
    return reference_labels

def train(k:int) -> dict:
    # from the mnist data load the train data
    (x_train, y_train), _ = mnist.load_data()
    # flat the images train data from 2 dim to one
    x_normalized = x_train.astype(float) / 255.
    x_flat = x_normalized.reshape(len(x_train), -1)

    kmeans = KMeans(n_clusters=k)
    clusters = kmeans.fit_predict(x_flat)
    reference_labels = retrieve_image_info(kmeans.labels_, y_train)
    # get the centroids of each cluster and reshape it back to 2-dim (image)
    centroids = kmeans.cluster_centers_.reshape(k, 28, 28) * 255

    return generate_response(centroids, reference_labels, k, clusters, x_train)

