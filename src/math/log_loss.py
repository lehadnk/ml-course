from collections import Counter, defaultdict
from math import log


def log_loss(ys, ps):
    - 1 / len(ys) * sum([y * log(ps) + (1 - y) * log(1 - p) for y, p in zip(ys, ps)])