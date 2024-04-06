import math

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class EuclideanDistanceCalculator(AbstractDistanceCalculator):
    def distance_between(self, point1: list, point2: list) -> float:
        if len(point1) != len(point2):
            raise ValueError("Length of point1 and point2 is not equal")

        distance = 0
        for i in range(len(point1)):
            distance += (point1[i] - point2[i]) ** 2

        return math.sqrt(distance)
