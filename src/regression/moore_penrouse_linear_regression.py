import numpy as np

from src.regression.abstract_regressor import AbstractRegressor


class MoorePenrouseLinearRegression(AbstractRegressor):
    def __init__(self):
        self.b = 0
        self.w = []

    def fit(self, X, Y):
        X_with_bias = [[1] + x for x in X]
        coefficients = np.linalg.pinv(X_with_bias) @ np.array(Y)
        self.b = coefficients[0]
        self.w = coefficients[1:]

    def predict(self, X):
        return self.b + sum(x * w for x, w in zip(self.w, X))