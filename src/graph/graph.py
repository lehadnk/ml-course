from typing import Optional, List

from src.distance.abstract_distance_calculator import AbstractDistanceCalculator


class BidirectionalEdge():
    def __init__(self, n1: int, n2: int, weight: float):
        self.n1 = n1
        self.n2 = n2
        self.weight = weight

    def __repr__(self):
        return f"({self.n1}, {self.n2}, {self.weight})"

class BidirectionalGraph:
    def __init__(self, edges: Optional[List[BidirectionalEdge]]):
        self.edge_list = []
        self.edge_map = {}

        if edges is not None:
            for edge in edges:
                self.add_edge(edge)

    def add_edge(self, edge: BidirectionalEdge):
        self.edge_list.append(edge)
        if edge.n1 not in self.edge_map:
            self.edge_map[edge.n1] = {}
        if edge.n2 not in self.edge_map[edge.n1]:
            self.edge_map[edge.n1][edge.n2] = []

        self.edge_map[edge.n1][edge.n2].append(edge)

        if edge.n2 not in self.edge_map:
            self.edge_map[edge.n2] = {}
        if edge.n1 not in self.edge_map[edge.n2]:
            self.edge_map[edge.n2][edge.n1] = []

        self.edge_map[edge.n2][edge.n1].append(edge)

    def get_edges_from(self, node_id: int) -> List[BidirectionalEdge]:
        if self.edge_map[node_id] is None:
            return []

        result = []
        for n2 in self.edge_map[node_id].values():
            for edge in n2:
                result.append(edge)

        return result

    def get_edges_to(self, node_id: int) -> List[BidirectionalEdge]:
        # In bidirectional graph it's the same as from list
        return self.get_edges_from(node_id)

    def remove_edge(self, edge: BidirectionalEdge):
        self.edge_list.remove(edge)
        self.edge_map[edge.n1][edge.n2].remove(edge)
        self.edge_map[edge.n2][edge.n1].remove(edge)

    def get_shortest_edge(self, n1: int, n2: int) -> Optional[BidirectionalEdge]:
        if n1 not in self.edge_map:
            return None
        if n2 not in self.edge_map[n1]:
            return None

        shortest_edge = None
        for edge in self.edge_map[n1][n2]:
            if shortest_edge is None or edge.weight < shortest_edge.weight:
                shortest_edge = edge

        return shortest_edge

    def get_longest_edge(self, n1: int, n2: int) -> Optional[BidirectionalEdge]:
        if n1 not in self.edge_map:
            return None
        if n2 not in self.edge_map[n1]:
            return None

        shortest_edge = None
        for edge in self.edge_map[n1][n2]:
            if shortest_edge is None or edge.weight > shortest_edge.weight:
                shortest_edge = edge

        return shortest_edge

    def delete_edges_longer_than(self, weight: float):
        edges_to_delete = []
        for edge in self.edge_list:
            if edge.weight > weight:
                edges_to_delete.append(edge)

        for edge in edges_to_delete:
            self.remove_edge(edge)

    def get_edges_between(self, n1: int, n2: int) -> List[BidirectionalEdge]:
        if n1 not in self.edge_map:
            return []
        if n2 not in self.edge_map[n1]:
            return []

        return self.edge_map[n1][n2]

    def add_node(self, node_id: int):
        if not node_id in self.edge_map:
            self.edge_map[node_id] = {}
    def remove_node(self, node_id: int):
        for edge in self.edge_list:
            if edge.n1 == node_id or edge.n2 == node_id:
                self.remove_edge(edge)

        del self.edge_map[node_id]

        for key in self.edge_map.keys():
            del self.edge_map[key][node_id]

    def get_nodes(self) -> List[int]:
        return list(self.edge_map.keys())

    def is_cyclic(self):
        visited = {}

        def dfs_visit(node_id: int, parent_node_id: Optional[int]) -> bool:
            visited[node_id] = True

            edges = self.get_edges_from(node_id)
            for edge in edges:
                if edge.n1 == node_id:
                    this, that = edge.n1, edge.n2
                else:
                    that, this = edge.n1, edge.n2

                if that == parent_node_id:
                    continue

                if visited[that]:
                    return True

                if dfs_visit(that, this):
                    return True

            return False

        # It's not optimal to traverse from every node, and it's better to dfs split for clusters and traverse each cluster once, but I'm too lazy to refactor circular reference in modules now
        for node_id in self.get_nodes():
            for nid in self.get_nodes():
                visited[nid] = False

            if dfs_visit(node_id, None):
                return True

        return False
        # return not (len(cycle_is_found) == 0)

    def get_weight(self) -> int:
        return sum(edge.weight for edge in self.edge_list)

def dataset_to_graph(dataset: list, distance_calculator: AbstractDistanceCalculator) -> BidirectionalGraph:
    graph = BidirectionalGraph(None)

    for i in range(len(dataset)):
        for j in range(len(dataset)):
            # We should only process each pair once, so for [1, 2, 3] we connect 1 - 2, 1 - 3, then 2 - 3
            if i >= j:
                continue

            graph.add_edge(BidirectionalEdge(i, j, distance_calculator.distance_between(dataset[i], dataset[j])))

    return graph


# class Edge:
#     def __init__(self, start: int, end: int, distance: float):
#         self.start = start
#         self.end = end
#         self.distance = distance
#
#     def __repr__(self):
#         return f"({self.start}, {self.end}, {self.distance})"

# class Node:
#     def __init__(self, id: int):
#         self.id = id

# class Graph:
#     def __init__(self):
#         self.edges = {}
#         self.nodes = {}
#
#     def add_node(self, node: Node):
#         if self.nodes.get(node.id) is not None:
#             raise f"Node with id {node.id} already exists"
#
#         self.nodes[node.id] = node
#
#     def get_node(self, id: int) -> Optional[Node]:
#         return self.nodes.get(id)
#
#     def add_bidirectional_edge(self, node_id1: int, node_id2: int, distance: float):
#         self.add_edge(Edge(node_id1, node_id2, distance))
#         self.add_edge(Edge(node_id2, node_id1, distance))
#
#     def add_edge(self, edge: Edge):
#         if self.edges.get(edge.start) is None:
#             self.edges[edge.start] = {}
#
#         if self.edges[edge.start].get(edge.end) is None:
#             self.edges[edge.start][edge.end] = []
#
#         self.edges[edge.start][edge.end].append(edge)
#
#     def get_edges_from(self, start: int):
#         if self.edges.get(start) is None:
#             return []
#
#         edge_list = []
#         for k, edges in self.edges[start].items():
#             for edge in edges:
#                 edge_list.append(edge)
#
#         return edge_list
#
#     def get_edges_to(self, end: int):
#         edge_list = []
#         for k1, v1 in self.edges.items():
#             for k2, v2 in self.edges[k1].items():
#                 if k2 == end:
#                     edge_list.append(edge for edge in self.edges[k1][k2])
#
#         return edge_list
#
#     def get_edges(self, start: int, end: int) -> List[Edge]:
#         if self.edges.get(start) is None:
#             return []
#
#         if self.edges[start].get(end) is None:
#             return []
#
#         return self.edges[start][end]
#
#     def get_shortest_edge(self, start: int, end: int) -> Optional[Edge]:
#         shortest_edge = None
#         for edge in self.get_edges(start, end):
#             if shortest_edge is None or edge.distance < shortest_edge.distance:
#                 shortest_edge = edge
#
#         return shortest_edge
#
#     def get_longest_edge(self, start: int, end: int) -> Optional[Edge]:
#         longest_edge = None
#         for edge in self.get_edges(start, end):
#             if longest_edge is None or edge.distance > longest_edge.distance:
#                 longest_edge = edge
#
#         return longest_edge
#
#     def delete_edges_longer_than(self, distance: float):
#         for k1 in self.edges.keys():
#             for k2 in self.edges[k1].keys():
#                 for edge in self.edges[k1][k2]:
#                     if edge.weight > distance:
#                         self.edges[k1][k2].remove(edge)
#
#     def get_edge_list(self) -> List[Edge]:
#         edge_list = []
#         for k1 in self.edges.keys():
#             for k2 in self.edges[k1].keys():
#                 for edge in self.edges[k1][k2]:
#                     edge_list.append(edge)
#
#         return edge_list
#
#     def get_weight(self):
#         return sum(edge.distance for edge in self.get_edge_list())
#
#     def is_cyclic(self) -> bool:
#         node_id = next(iter(self.nodes)).id
#
#         return True