from typing import Optional

from src.graph.dfs import deep_first_search
from src.graph.graph import BidirectionalGraph
from src.graph.mst.kruskal import kruskal_mst


def clusterize_dfs(graph: BidirectionalGraph, max_distance: Optional[float]):
    if max_distance is not None:
        graph.delete_edges_longer_than(max_distance)

    clusterized = {}
    for node_id in graph.get_nodes():
        clusterized[node_id] = False

    def first_unclusterized_node_id():
        for k, v in clusterized.items():
            if not v:
                return k

        return None

    clusters = []
    node_id = first_unclusterized_node_id()
    while node_id is not None:
        node_ids_in_cluster = deep_first_search(graph, node_id)
        clusters.append(node_ids_in_cluster)
        for node_id in node_ids_in_cluster:
            clusterized[node_id] = True

        node_id = first_unclusterized_node_id()

    return clusters

def clusterize_using_mst(graph: BidirectionalGraph, clusters: int):
    mst = kruskal_mst(graph)
    mst.edge_list.sort(key=lambda x: x.weight, reverse=True)
    for i in range(0, clusters - 1):
        mst.remove_edge(mst.edge_list[0])

    return clusterize_dfs(mst, None)