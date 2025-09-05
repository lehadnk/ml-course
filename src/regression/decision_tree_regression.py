from typing import List

from src.math.average import average


class DecisionTreeNode:
    def __init__(self):
        self.feature = None
        self.threshold = None
        self.left = None
        self.right = None

class DecisionTreeBucket:
    def __init__(self, values: List[DecisionTreeNode]):
        self.values = values

    def value(self):
        return average(self.values)

class DecisionTreeRegressor:
    def __init__(self):
        self.root = None

    def fit(self, X, Y):
        if len(X) != len(Y):
            raise ValueError("X and Y must have same length")
        if len(X) == 0:
            raise ValueError("X cannot be empty")

        self.root = self._fit(X, Y)

    def _fit(self, X, Y):
        selected_feature = None
        selected_threshold_value = None
        selected_index = None

        if len(X) > 2:
            average_y = average(Y)
            selected_mse = sum([(y - average_y) ** 2 for y in Y]) / len(Y)
            for f in range(len(X[0])):
                pairs = sorted(zip([x[f] for x in X], Y), key=lambda x: x[0])
                Xs, Ys = zip(*pairs)
                for i in range(len(Y) - 1):
                    Y_left = Ys[:i + 1]
                    Y_right = Ys[i + 1:]
                    Y_avg_left = average(Y_left)
                    Y_avg_right = average(Y_right)
                    mse_left = sum((y - Y_avg_left) ** 2 for y in Y_left) / len(Y_left)
                    mse_right = sum((y - Y_avg_right) ** 2 for y in Y_right) / len(Y_right)
                    mse = mse_left + mse_right

                    if mse < selected_mse:
                        selected_feature = f
                        selected_threshold_value = (Xs[i] + Xs[i + 1]) / 2
                        selected_mse = mse_left + mse_right
                        selected_index = i

        if selected_feature is None:
            return DecisionTreeBucket(Y)

        pairs = sorted(zip(X, Y), key=lambda x: x[0][selected_feature])
        Xs, Ys = zip(*pairs)
        node = DecisionTreeNode()
        node.feature = selected_feature
        node.threshold = selected_threshold_value
        node.left = self._fit(Xs[:selected_index + 1], Ys[:selected_index + 1])
        node.right = self._fit(Xs[selected_index + 1:], Ys[selected_index + 1:])
        return node

    def predict(self, X):
        results = []
        self._predict(X, results, self.root)
        return average(results)

    def _predict(self, X, results, node):
        if isinstance(node, DecisionTreeBucket):
            results.extend(node.values)
            return

        if X[node.feature] is None:
            self._predict(X, results, node.left)
            self._predict(X, results, node.right)
        else:
            if X[node.feature] < node.threshold:
                self._predict(X, results, node.left)
            else:
                self._predict(X, results, node.right)