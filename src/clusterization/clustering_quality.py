from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


def get_clustering_quality(clusters: list, dimensions: int, dc: AbstractDistanceCalculator) -> list:
    distances = []
    for i in range(len(clusters)):
        cluster_center = [0] * dimensions
        for point in clusters[i]:
            for j in range(dimensions):
                cluster_center[j] += point[j]

        cluster_center = [x / len(clusters[i]) for x in cluster_center]

        sum_distance = 0
        for point in clusters[i]:
            sum_distance += dc.distance_between(point, cluster_center)

        distances.append(sum_distance / len(clusters[i]))

    return distances