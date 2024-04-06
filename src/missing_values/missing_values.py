from src.distance.abstract_distance_calculator import AbstractDistanceCalculator
from src.math.average import average
from src.math.correlation import pearson_correlation_coefficient


def fill_missing_value_in_row_using_pearson(attributes: list, row: list):
    column_index = row.index(None)
    corellation_indicies = [abs(pearson_correlation_coefficient(attributes[column_index], a)) for a in attributes]
    averages = [average(a) for a in attributes]

    a = 1 / sum(corellation_indicies[i] for i in range(0, len(corellation_indicies)) if i != column_index)
    b = sum(corellation_indicies[i] * abs(row[i] - averages[i]) for i in range(0, len(corellation_indicies)) if i != column_index)
    return averages[column_index] + a * b

def fill_missing_value_in_row_using_nearest_neighbors(dc: AbstractDistanceCalculator, dataset: list, row: list):
    column_index = row.index(None)
    closest_entry_index = dc.closest_to(dataset, row)

    return dataset[closest_entry_index][column_index]
