import numpy as np
import pandas as pd
import json
import da_tool.tca
from tl_algs import tl_alg
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import euclidean_distances

class TCA(tl_alg.Base_Transfer):
        def __init__(self, test_set_X, test_set_domain, train_pool_X, train_pool_y,
                 train_pool_domain, Base_Classifier, classifier_params={},
                 rand_seed=None, dims=5, kernel_type='linear', kernel_param=1,
                mu=1):

        super(TCA, self).__init__(
            test_set_X,
            test_set_domain,
            train_pool_X,
            train_pool_y,
            train_pool_domain,
            Base_Classifier,
            rand_seed=rand_seed,
            classifier_params=classifier_params,
        )

        self.dims = dims
        self.kernel_type = kernel_type
        self.kernel_param = kernel_param
        self.mu = mu

    def create_classifier(self, X_train, y_train):
        my_tca = da_tool.tca.TCA(dim=self.dims,kerneltype=self.kernel_type,
                kernelparam=self.kernel_param, mu=self.mu)
        train_TCA_X, target_test_TCA_X, __ = \
            my_tca.fit_transform(X_train, self.test_set_X)

        # build and train classifier
        clf = self.Base_Classifier(random_state=self.rand_seed,
                **self.classifier_params)
        clf.fit(train_TCA_X, y_train)
        return clf.predict(target_test_TCA_X)

    def train_filter_test(self):
        pred_list = []
        for proj in set(self.train_pool_domain):
            X_train_subset = self.train_pool_X[
                np.array(self.train_pool_domain) == proj]
            y_train_subset = self.train_pool_y[X_train_subset.index]
            predictions = self.create_classifier(X_train_subset, y_train_subset)
            pred_list.append(predictions)

        # average votes
        votes = zip(*pred_list)
        confidence_arr = np.mean(votes, 1)
        predictions_arr = confidence_arr > 0.5
        return (confidence_arr, np.array(predictions_arr))

    def json_encode(self):
        base = tl_alg.Base_Transfer.json_encode(self)
        base.update({"dims" : self.dims,
            "kernel_type" : self.kernel_type,
            "kernel_param" : self.kernel_param,
            "mu" : self.mu})

        return base
