import numpy as np
from scipy.io import loadmat


def load_newhome(scale=True, usps=False, all_use=False):
    newhome_data = loadmat('data/newhome.mat')
    if scale:
        newhome_train = np.reshape(newhome_data['train_32'], (55000, 32, 32, 1))
        newhome_test = np.reshape(newhome_data['test_32'], (10000, 32, 32, 1))
        newhome_train = np.concatenate([newhome_train, newhome_train, newhome_train], 3)
        newhome_test = np.concatenate([newhome_test, newhome_test, newhome_test], 3)
        newhome_train = newhome_train.transpose(0, 3, 1, 2).astype(np.float32)
        newhome_test = newhome_test.transpose(0, 3, 1, 2).astype(np.float32)
        newhome_labels_train = newhome_data['label_train']
        newhome_labels_test = newhome_data['label_test']
    else:
        newhome_train = newhome_data['train_28']
        newhome_test =  newhome_data['test_28']
        newhome_labels_train = newhome_data['label_train']
        newhome_labels_test = newhome_data['label_test']
        newhome_train = newhome_train.astype(np.float32)
        newhome_test = newhome_test.astype(np.float32)
        newhome_train = newhome_train.transpose((0, 3, 1, 2))
        newhome_test = newhome_test.transpose((0, 3, 1, 2))
    train_label = np.argmax(newhome_labels_train, axis=1)
    inds = np.random.permutation(newhome_train.shape[0])
    newhome_train = newhome_train[inds]
    train_label = train_label[inds]
    test_label = np.argmax(newhome_labels_test, axis=1)
    if usps and all_use != 'yes':
        newhome_train = newhome_train[:2000]
        train_label = train_label[:2000]

    return newhome_train, train_label, newhome_test, test_label
