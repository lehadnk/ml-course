from src.math.average import average
from src.math.stdev import stdev
from src.math.symmetry import is_symmetrical


def is_outlier(vector: list, index: int) -> bool:
    vector_without_value = vector.copy()
    del(vector_without_value[index])

    stdv = stdev(vector_without_value)
    avg = average(vector_without_value)

    mod = 3 if is_symmetrical(vector_without_value) else 5

    if avg - mod * stdv < vector[index] < avg + mod * stdv:
        return False

    return True


