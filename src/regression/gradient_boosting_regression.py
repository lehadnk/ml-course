from src.regression.abstract_regressor import AbstractRegressor


class GradientBoostingRegressor(AbstractRegressor):
    def __init__(self, ensemble: list[AbstractRegressor]):
        self.ensemble = ensemble
        self.learning_rate = 0.1
        self.average = 0

    def fit(self, X, Y):
        if len(X) != len(Y):
            raise ValueError("X and Y must have same length")

        self.average = sum(Y) / len(Y)
        Ydiff = [y - self.average for y in Y]
        for regressor in self.ensemble:
            regressor.fit(X, Ydiff)
            for i in range(len(X)):
                Ydiff[i] -= regressor.predict(X[i]) * self.learning_rate

    def predict(self, X):
        y = self.average
        for regressor in self.ensemble:
            y += regressor.predict(X) * self.learning_rate

        return y