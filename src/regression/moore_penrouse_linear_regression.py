import numpy as np
class MoorePenrouseLinearRegression:
    def __init__(self, data):
        X = np.array([[1, point[0], point[1]] for point in data])
        Z = np.array([point[2] for point in data])

        self.coefficients = np.linalg.pinv(X) @ Z

    def predict(self, point):
        return self.coefficients[0] + sum([point[i - 1] * self.coefficients[i] for i in range(1, len(self.coefficients))])