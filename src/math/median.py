def median(vector: list) -> float:
    sorted_vector = vector.copy()
    sorted_vector.sort()
    if len(sorted_vector) % 2 == 1:
        return sorted_vector[int(len(sorted_vector) / 2)]

    return (sorted_vector[int(len(sorted_vector) / 2) - 1] + sorted_vector[int(len(sorted_vector) / 2)]) / 2
