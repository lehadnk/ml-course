import math

from src.math.deviation import sq_deviation


def stdev(vector: list) -> float:
    n = len(vector)
    return math.sqrt((1 / (n - 1)) * sum(sq_deviation(vector)))
