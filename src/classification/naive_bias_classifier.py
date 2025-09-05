import math
import unittest
from collections import defaultdict


class NaiveBiasClassifier():
    def __init__(self):
        self.X = []
        self.y = []
        self.y_probs = {}

    def fit(self, X, y):
        assert len(X) == len(y)
        self.X = X
        self.y = y

        cnt = defaultdict(int)
        for y in self.y:
            cnt[y] += 1

        self.y_probs = {}
        for v, c in cnt.items():
            self.y_probs[v] = c / float(len(self.y))

    def get_prediction_scores(self, X):
        log_scores = {}
        for y, y_prob in self.y_probs.items():
            filtered_xs = [xi for xi, yi in zip(self.X, self.y) if yi == y]
            for i in range(len(X)):
                score = len([x for x in filtered_xs if x[i] == X[i]]) / len(filtered_xs)
                if log_scores.get(y) is None:
                    log_scores[y] = score
                else:
                    log_scores[y] *= score

            log_scores[y] *= y_prob

        sum_log_scores = sum(log_scores.values())
        return {y: v / sum_log_scores for y, v in log_scores.items()}

    def predict(self, X):
        scores = self.get_prediction_scores(X)
        return max(scores.items(), key=lambda item: item[1])[0]