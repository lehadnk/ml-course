from typing import List

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator

class KnnElement:
    def __init__(self, location: List[float], cls: str):
        self.location = location
        self.cls = cls

class KnnClassifier:
    def __init__(self, distance_calculator: AbstractDistanceCalculator, k: int):
        self._distance_calculator = distance_calculator
        self._k = k
        self._elements = []

    def add(self, location: List[float], cls: str):
        self._elements.append(KnnElement(location, cls))

    def classify(self, location: List[float]) -> str:
        distance_list = []
        for element in self._elements:
            distance_list.append([self._distance_calculator.distance_between(element.location, location), element.cls])

        sorted_distance_list = sorted(distance_list, key=lambda x: x[0])
        if len(sorted_distance_list) > self._k:
            sorted_distance_list = sorted_distance_list[:self._k]

        classes = {}
        for distance, cls in sorted_distance_list:
            if cls not in classes:
                classes[cls] = 1
            else:
                classes[cls] += 1

        return max(classes, key=classes.get)