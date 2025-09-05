from src.regression.abstract_regressor import AbstractRegressor


class LinearRegressor(AbstractRegressor):
    def __init__(self):
        self.w = []
        self.b = 0

    def fit(self, X, Y):
        num_axes = len(X[0])
        axis_values = [[x[a] for x in X] for a in range(num_axes)]
        averages = [sum(axis_values[i]) / len(axis_values[i]) for i in range(num_axes)]
        y_average = sum(Y) / len(Y)

        X_deviations = [[x - averages[i] for x in axis_values[i]] for i in range(num_axes)]
        Y_deviations = [y - y_average for y in Y]

        numerators = [sum([X_deviations[i][j] * Y_deviations[j] for j in range(len(X))]) for i in range(num_axes)]
        denumerators = [sum([X_deviations[i][j] ** 2 for j in range(len(X))]) for i in range(num_axes)]

        self.w = [numerators[i] / denumerators[i] if denumerators[i] != 0 else 0 for i in range(num_axes - 1)]
        self.b = y_average - sum([self.w[i] * averages[i] for i in range(num_axes - 1)])

    def predict(self, X):
        return sum(w * x for w, x in zip(self.w, X)) + self.b