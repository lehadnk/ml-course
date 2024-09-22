from typing import List


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

    def distance_to_all(self, dataset: List[List[float]]) -> List[List[float]]:
        result = []
        for row in dataset:
            distances = []
            for other_row in dataset:
                distances.append(self.distance_between(row, other_row))
            result.append(distances)

        return result

    def distance_sum_to_all(self, dataset: List[List[float]]) -> List[float]:
        distances = self.distance_to_all(dataset)
        return [sum(distances) for distances in distances]
