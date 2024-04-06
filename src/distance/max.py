from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class MaxDistanceCalculator(AbstractDistanceCalculator):
    def distance_between(self, point1: list, point2: list) -> float:
        if len(point1) != len(point2):
            raise ValueError("Length of point1 and point2 is not equal")

        max_distance = 0
        for i in range(len(point1)):
            d = abs(point1[i] - point2[i])
            if d > max_distance:
                max_distance = d

        return max_distance
