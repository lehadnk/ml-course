from src.math.average import average
from src.math.stdev import stdev


def normalize_using_min_max(vector: list):
    min_value = min(vector)
    max_value = max(vector)

    return [(v - min_value) / (max_value - min_value) for v in vector]

def normalize_using_avg_and_stdev(vector: list):
    avg = average(vector)
    stdev_value = stdev(vector)

    return [(v - avg) / stdev_value for v in vector]
