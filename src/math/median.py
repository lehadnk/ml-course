def median(vector: list) -> float:
    sorted_vector = vector.copy()
    sorted_vector.sort()
    if len(sorted_vector) % 2 == 1:
        return sorted_vector[int(len(sorted_vector) / 2)]

    return (sorted_vector[int(len(sorted_vector) / 2) - 1] + sorted_vector[int(len(sorted_vector) / 2)]) / 2

def quartile25(vector: list) -> float:
    md = median(vector)
    filtered_list = list(filter(lambda v : v < md, vector))

    return median(filtered_list)

def quartile75(vector: list) -> float:
    md = median(vector)
    filtered_list = list(filter(lambda v: v > md, vector))

    return median(filtered_list)

def filter_outside_quartile2575(vector: list) -> list:
    q25 = quartile25(vector)
    q75 = quartile75(vector)

    q25th = q25 - 1.5 * (q75 - q25)
    q75th = q75 + 1.5 * (q75 - q25)

    return list(filter(lambda v : q25th < v < q75th, vector))