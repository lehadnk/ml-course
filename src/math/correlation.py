import math

from src.math.average import average
from src.math.deviation import deviation, sq_deviation


def pearson_correlation_coefficient(vector1: list, vector2: list) -> float:
    avg1 = average(vector1)
    avg2 = average(vector2)

    sqdv1 = sq_deviation(vector1)
    sqdv2 = sq_deviation(vector2)

    sq_deviation_sum_vector1 = sum(sqdv1)
    sq_deviation_sum_vector2 = sum(sqdv2)

    numerator = sum([(avg1 - vector1[i]) * (avg2 - vector2[i]) for i in range(0, len(vector1))])
    denominator = math.sqrt(sq_deviation_sum_vector1 * sq_deviation_sum_vector2)
    return numerator / denominator
