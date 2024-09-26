import random

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class KmeansClusterizer():
    def __init__(self, dataset: list):
        if len(dataset) == 0:
            raise ValueError("Kmeans cannot have an empty dataset")

        self.dataset = dataset
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

    def kmeans_clustering(self, points_count: int, dc: AbstractDistanceCalculator) -> dict:
        cluster_centers = []
        for i in range(points_count):
            cluster_centers.append(self.get_random_point())

        last_cluster_centers = None
        points_affinity = {}
        for i in range(points_count):
            points_affinity[i] = []

        while True:
            for point in self.dataset:
                distances = []
                for i in range(points_count):
                    distances.append(dc.distance_between(point, cluster_centers[i]))
                nearest_cluster = distances.index(min(distances))
                points_affinity[nearest_cluster].append(point)

            last_cluster_centers = cluster_centers.copy()
            for i in range(points_count):
                coordinates = [0] * self.dimensions
                for point in points_affinity[i]:
                    coordinates = [x + y for x, y in zip(point, coordinates)]

                cluster_centers[i] = [coordinates[i] / len(points_affinity[i]) if len(points_affinity[i]) > 0 else 0 for i in range(points_count)]

            for i in range(points_count):
                for j in range(self.dimensions):
                    if cluster_centers[i][j] != last_cluster_centers[i][j]:
                        continue

            return points_affinity