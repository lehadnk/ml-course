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
    missing_column_index = row.index(None)
    ds_without_missing_column = [[ds_row[i] for i in range(0, len(ds_row)) if i != missing_column_index] for ds_row in dataset]
    row_without_missing_column = [row[i] for i in range(0, len(row)) if i != missing_column_index]

    closest_entry_index = dc.closest_to(ds_without_missing_column, row_without_missing_column)

    return dataset[closest_entry_index][missing_column_index]
