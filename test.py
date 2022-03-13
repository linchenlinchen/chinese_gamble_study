# this is a code test
from time import time
import numpy as np
import matplotlib.pyplot as plt
import pickle
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn import datasets
from sklearn.manifold import TSNE


def get_test_data():
    data = np.array([
        [1, 2, 3, 4, 5, 6],
        [2, 2, 2, 2, 2, 2],
        [0, 0, 1, 2, 1, 1]
    ])
    MAX_LEN = 3
    label = np.array([[1], [1], [4]])
    # ohe = OneHotEncoder()
    # label = ohe.fit_transform(label).toarray()
    n_samples, n_features = data.shape
    print(f"n_sample {n_samples}, n_features: {n_features}")
    return data, label, n_samples, n_features


def plot_embedding(data, label, title):
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)

    fig = plt.figure()
    ax = plt.subplot(111)
    for i in range(data.shape[0]):
        plt.text(data[i, 0], data[i, 1], int(label[i]),
                 color=plt.cm.Set1(int(label[i]) / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    plt.xticks([])
    plt.yticks([])
    plt.title(title)
    return fig


def main():
    data, label, n_samples, n_features = get_test_data()
    print('Computing t-SNE embedding')
    tsne = TSNE(n_components=2, init='pca', random_state=0)
    t0 = time()
    result = tsne.fit_transform(data)
    plt.scatter(result[:,0],result[:,1])
    # fig = plot_embedding(result, label,'t-SNE embedding of the digits (time %.2fs)' % (time() - t0))
    plt.show()


if __name__ == '__main__':
    main()

