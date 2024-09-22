import math

from src.math.average import average
from src.math.median import median
from src.math.stdev import stdev


def is_symmetrical(vector: list) -> bool:
    avg = average(vector)
    md = median(vector)

    return abs(avg - md) <= (3 * stdev(vector)) / math.sqrt(len(vector))