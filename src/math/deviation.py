from src.math.average import average


def deviation(vector: list) -> list:
    avg = average(vector)
    return [v - avg for v in vector]

def sq_deviation(vector: list) -> list:
    avg = average(vector)
    return [(v - avg) ** 2 for v in vector]
