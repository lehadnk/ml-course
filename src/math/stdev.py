import math

from src.math.deviation import sq_deviation


def stdev(vector: list) -> float:
    if len(vector) < 2:
        raise ValueError("stdev requires at least 2 elements in vector")

    n = len(vector)
    return math.sqrt((1 / (n - 1)) * sum(sq_deviation(vector)))
