import numpy as np
import time

class my_kmeans:
    def __init__(self, k=3, n_init=10, seed=None):
        self.k = k
        self.n_init = n_init
        self.seed = seed

        self.X = None
        self.l_norm = 2
        self.max_steps = 500
        self.centers = None
        self.labels = None
        self.S = None  # matrix of l2 norm distance
        self.wcss = 0  # within cluster sum of squares (wcss)

        self.best_wcss = np.inf
        self.best_labels = None

    def init_centers(self):
        rng = np.random.default_rng(self.seed)
        samples = rng.choice(len(self.X), size=self.k, replace=False)
        self.centers = self.X[samples, :]

    def compute_norm(self):
        m = len(self.X)
        k = len(self.centers)

        self.S = np.empty((m, k))

        for i in range(m):
            self.S[i, :] = np.linalg.norm(self.X[i, :] - self.centers, ord=self.l_norm, axis=1) ** 2

    def assign_cluster_labels(self):
        self.labels = np.argmin(self.S, axis=1)

    def update_centers(self):
        m, d = self.X.shape

        ks = []
        k_max = int(max(self.labels) + 1)
        for j in range(k_max):
            if len(self.X[self.labels == j, :]) > 0:
                ks.append(j)
            else:
                print(f"missing cluster {j}")

        self.centers = np.empty((int(len(ks)), d))
        for j, k in enumerate(ks):
            self.centers[j, :] = np.mean(self.X[self.labels == k, :], axis=0)

    def has_converged(self, old_centers):
        return set([tuple(x) for x in old_centers]) == set([tuple(x) for x in self.centers])

    def calculate_wcss(self):
        """ Calculate Within Cluster Sum of Squares (aka Inertia) """
        self.wcss = np.sum(np.amin(self.S, axis=1))

    def fit(self,
            X, k=3):

        self.X = X
        self.k = k

        for _ in range(self.n_init):
            self.init_centers()
            converged = False
            self.labels = np.zeros(len(self.X))
            i = 1
            while (not converged) and (i <= self.max_steps):
                old_centers = self.centers

                self.compute_norm()
                self.assign_cluster_labels()
                self.update_centers()
                if self.has_converged(old_centers):
                    converged = True

                self.k = self.centers.shape[0]
                i += 1
            self.calculate_wcss()
            if self.wcss < self.best_wcss:
                self.best_wcss = self.wcss
                self.best_labels = self.labels
