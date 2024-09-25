from typing import List

from src.graph.graph import BidirectionalGraph


def deep_first_search(graph: BidirectionalGraph, start: int) -> List[int]:
    # Deep First Search Algorithm
    # Returns the list of node ids within the connected graph component

    visited = {}
    for node_id in graph.get_nodes():
        visited[node_id] = False

    def dfs_visit(node_id: int):
        visited[node_id] = True

        edges = graph.get_edges_from(node_id)
        for edge in edges:
            if not visited[edge.n2]:
                dfs_visit(edge.n2)

    dfs_visit(start)

    result = []
    for k, v in visited.items():
        if v:
            result.append(k)

    return result