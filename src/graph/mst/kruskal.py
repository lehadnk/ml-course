from src.graph.graph import BidirectionalGraph


def kruskal_mst(graph: BidirectionalGraph) -> BidirectionalGraph:
    # Kruskal's implementation of minimum spanning tree
    graph.edge_list.sort(key=lambda x: x.weight)

    mst = BidirectionalGraph(None)

    i = 0
    while len(mst.edge_list) < len(graph.get_nodes()) - 1:
        candidate_edge = graph.edge_list[i]
        mst.add_edge(candidate_edge)
        if mst.is_cyclic():
            mst.remove_edge(candidate_edge)

        i += 1

    return mst