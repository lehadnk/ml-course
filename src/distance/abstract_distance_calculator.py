class AbstractDistanceCalculator:
    def distance_between(self, point1: list, point2: list) -> float:
        pass

    def closest_to(self, dataset: list, row: list) -> int:
        min_distance_index = -1
        min_distance = -1
        for ds_row_index, ds_row in enumerate(dataset):
            distance = self.distance_between(row, ds_row)
            if distance < min_distance or min_distance == -1:
                min_distance = distance
                min_distance_index = ds_row_index

        return min_distance_index
