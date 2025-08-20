from collections import Counter, defaultdict
from typing import Union, List

from src.tree.gini import gini_impurity

class GiniClassificationBucket:
    def __init__(self, Y):
        self.classes = defaultdict(int)
        for y in Y:
            self.classes[y] += 1

class GiniClassificationTreeNode:
    def __init__(self, attribute_number):
        self.attribute_number = attribute_number
        self.children = {}

    def to(self, attribute_value, target):
        self.children[attribute_value] = target

    def get(self, attribute_value):
        return self.children.get(attribute_value)

class GiniClassificationTree:
    def __init__(self):
        self.root = None

    def fit(self, X: List[List[int]], y):
        self.root = self.__fit(X, y, range(len(X[0])) if len(X) > 0 else [])

    def __fit(self, X, y, remaining_attributes: list):
        # We don't branch if all y values are the same
        if len(set(y)) == 1:
            return GiniClassificationBucket(y)

        # Also, if all X elements are the same, we stop branching
        X_remaining_attributes = [[x[i] for i in remaining_attributes] for x in X]
        if all(inner == X_remaining_attributes[0] for inner in X_remaining_attributes):
            return GiniClassificationBucket(y)

        if len(remaining_attributes) == 0:
            return GiniClassificationBucket(y)

        if len(remaining_attributes) == 1:
            current_attribute = remaining_attributes[0]
        else:
            remaining_attribute_vectors = [[x[i] for x in X] for i in remaining_attributes]
            gini_inpurity_coefficient_vector = [gini_impurity(v, y) for v in remaining_attribute_vectors]
            current_attribute = remaining_attributes[gini_inpurity_coefficient_vector.index(min(gini_inpurity_coefficient_vector))]

        node = GiniClassificationTreeNode(current_attribute)
        child_remaining_attributes = [i for i in remaining_attributes[:] if i != current_attribute]

        X_values = Counter([x[current_attribute] for x in X])
        for xv in X_values.keys():
            current_x_value_indices = [i for i, x in enumerate(X) if x[current_attribute] == xv]
            node.to(xv, self.__fit([X[i] for i in current_x_value_indices], [y[i] for i in current_x_value_indices], child_remaining_attributes))

        return node

    def predict(self, X):
        probs = defaultdict(int)
        self.__predict(self.root, X, probs)
        return max(probs, key=probs.get)

    def __predict(self, node: Union[GiniClassificationTreeNode, GiniClassificationBucket], X, probs):
        if type(node) is GiniClassificationBucket:
            for c in node.classes:
                probs[c] += node.classes[c]
                return

        child_node = node.get(X[node.attribute_number])
        if not child_node:
            # No such value in the training dataset - we have to check every single child
            for c in node.children.values():
                self.__predict(c, X, probs)

            return

        self.__predict(child_node, X, probs)