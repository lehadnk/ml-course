import math

from src.math.average import average
from src.math.stdev import stdev

def chauvenet_filter(vector: list) -> list:
    result = vector.copy()
    while True:
        has_outlier = False
        avg = average(result)
        stdv = stdev(result)
        for k, v in enumerate(result):
            erfc = math.erfc(abs(v - avg) / stdv)
            criteria = 1 / (2 * len(result))
            if erfc < criteria:
                del result[k]
                has_outlier = True
                break

        if not has_outlier:
            return result

        if len(result) < 2:
            return result
