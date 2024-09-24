from typing import Optional, List

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class Edge:
    def __init__(self, start: int, end: int, distance: float):
        self.start = start
        self.end = end
        self.distance = distance

class Node:
    def __init__(self, id: int):
        self.id = id

class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = {}

    def add_node(self, node: Node):
        if self.nodes.get(node.id) is not None:
            raise f"Node with id {node.id} already exists"

        self.nodes[node.id] = node

    def get_node(self, id: int) -> Optional[Node]:
        return self.nodes.get(id)

    def add_edge(self, edge: Edge):
        if self.edges.get(edge.start) is None:
            self.edges[edge.start] = {}

        if self.edges[edge.start].get(edge.end) is None:
            self.edges[edge.start][edge.end] = []

        self.edges[edge.start][edge.end].append(edge)

    def get_edges_from(self, start: int):
        if self.edges.get(start) is None:
            return []

        edge_list = []
        for k, edges in self.edges[start].items():
            for edge in edges:
                edge_list.append(edge)

        return edge_list

    def get_edges_to(self, end: int):
        edge_list = []
        for k1, v1 in self.edges.items():
            for k2, v2 in self.edges[k1].items():
                if k2 == end:
                    edge_list.append(edge for edge in self.edges[k1][k2])

        return edge_list

    def get_edges(self, start: int, end: int) -> List[Edge]:
        if self.edges.get(start) is None:
            return []

        if self.edges[start].get(end) is None:
            return []

        return self.edges[start][end]

    def get_shortest_edge(self, start: int, end: int) -> Optional[Edge]:
        shortest_edge = None
        for edge in self.get_edges(start, end):
            if shortest_edge is None or edge.distance < shortest_edge.distance:
                shortest_edge = edge

        return shortest_edge

    def get_longest_edge(self, start: int, end: int) -> Optional[Edge]:
        longest_edge = None
        for edge in self.get_edges(start, end):
            if longest_edge is None or edge.distance > longest_edge.distance:
                longest_edge = edge

        return longest_edge

    def delete_edges_longer_than(self, distance: float):
        for k1 in self.edges.keys():
            for k2 in self.edges[k1].keys():
                for edge in self.edges[k1][k2]:
                    if edge.distance > distance:
                        self.edges[k1][k2].remove(edge)

def dataset_to_graph(dataset: list, distance_calculator: AbstractDistanceCalculator) -> Graph:
    graph = Graph()

    for i in range(len(dataset)):
        graph.add_node(Node(i))

    for i in range(len(dataset)):
        for j in range(len(dataset)):
            if i == j:
                continue

            graph.add_edge(Edge(i, j, distance_calculator.distance_between(dataset[i], dataset[j])))

    return graph