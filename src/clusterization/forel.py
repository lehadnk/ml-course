import random
from unittest import result

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class ForelClusterizator:
    def __init__(self, dataset: list):
        if len(dataset) == 0:
            raise "Empty dataset"

        self.dataset = dataset
        self.clusters = []
        self.dimensions = len(dataset[0])

        self.field_size = []
        for i in range(self.dimensions):
            min, max = 0, 0
            for element in dataset:
                if element[i] < min:
                    min = element[i]
                if element[i] > max:
                    max = element[i]

            self.field_size.append((min, max))

    def get_random_point(self) -> list:
        point = []
        for i in self.field_size:
            point.append(random.randint(i[0], i[1]))

        return point

    def perform_clustering(self, range: float, distance_calculator: AbstractDistanceCalculator):
        last_cluster_points = []
        result = []
        forel = None
        while True:
            if forel is None:
                forel = self.get_random_point()

            cluster_points = []
            for i, element in enumerate(self.dataset):
                if distance_calculator.distance_between(forel, element) <= range:
                    cluster_points.append(i)

            if len(cluster_points) == 0:
                forel = None
                continue

            if len(cluster_points) == 0 or len(last_cluster_points) == 0:
                last_cluster_points = cluster_points.copy()
                continue

            # if len(last_cluster_points) == len(cluster_points):
            for cluster_point in cluster_points:
                if cluster_point not in last_cluster_points:
                    # Since the cluster had changed since the last adjustment, we adjust the forel point to the new center of the cluster
                    forel = [0] * self.dimensions
                    for point in cluster_points:
                        forel = [x + y for x, y in zip(forel, self.dataset[point])]

                    forel = [x / len(cluster_points) for x in forel]
                    last_cluster_points = cluster_points.copy()
                    continue

            cluster = []
            for point in cluster_points:
                cluster.append(self.dataset[point])

            for point in cluster:
                self.dataset.remove(point)

            result.append(cluster)
            forel = None

            if len(self.dataset) == 0:
                return result