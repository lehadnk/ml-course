class AbstractDistanceCalculator:
    def distance_between(self, point1: list, point2: list) -> float:
        pass

    def closest_to(self, dataset: list, row: list) -> int:
        missing_column_index = row.index(None)

        ds_without_missing_column = [[ds_row[i] for i in range(0, len(ds_row)) if i != missing_column_index] for ds_row in dataset]
        row_without_missing_column = [row[i] for i in range(0, len(row)) if i != missing_column_index]

        min_distance_index = -1
        min_distance = -1
        for ds_row_index, ds_row in enumerate(ds_without_missing_column):
            distance = self.distance_between(row_without_missing_column, ds_row)
            if distance < min_distance or min_distance == -1:
                min_distance = distance
                min_distance_index = ds_row_index

        return min_distance_index
