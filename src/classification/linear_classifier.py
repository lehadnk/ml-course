import numpy as np

class LinearClassifier:
    def __init__(self):
        self.w = None

    def fit(self, X, y):
        X = np.column_stack([X, np.ones_like(X)])  # [x, 1]
        Y = np.diag(y)

        # Quadratic problem: min ||1 - Y X w||^2
        # Solve by least squares: w = argmin ||(Y X) w - 1||^2
        A = Y @ X
        b = np.ones_like(y)
        w, *_ = np.linalg.lstsq(A, b, rcond=None)
        self.w = w

    def predict(self, X):
        return 1 if sum([X[i] * self.w[i] for i in range(len(X))]) + self.w[-1] > 0 else -1