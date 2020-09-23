import numpy as np
from scipy.io import loadmat


def load_home(scale=True, usps=False, all_use=False):
    home_data = loadmat('data/home.mat')
    if scale:
        home_train = np.reshape(home_data['train_32'], (55000, 32, 32, 1))
        home_test = np.reshape(home_data['test_32'], (10000, 32, 32, 1))
        home_train = np.concatenate([home_train, home_train, home_train], 3)
        home_test = np.concatenate([home_test, home_test, home_test], 3)
        home_train = home_train.transpose(0, 3, 1, 2).astype(np.float32)
        home_test = home_test.transpose(0, 3, 1, 2).astype(np.float32)
        home_labels_train = home_data['label_train']
        home_labels_test = home_data['label_test']
    else:
        home_train = home_data['train_28']
        home_test =  home_data['test_28']
        home_labels_train = home_data['label_train']
        home_labels_test = home_data['label_test']
        home_train = home_train.astype(np.float32)
        home_test = home_test.astype(np.float32)
        home_train = home_train.transpose((0, 3, 1, 2))
        home_test = home_test.transpose((0, 3, 1, 2))
    train_label = np.argmax(home_labels_train, axis=1)
    inds = np.random.permutation(home_train.shape[0])
    home_train = home_train[inds]
    train_label = train_label[inds]
    test_label = np.argmax(home_labels_test, axis=1)
    if usps and all_use != 'yes':
        home_train = home_train[:2000]
        train_label = train_label[:2000]

    return home_train, train_label, home_test, test_label
