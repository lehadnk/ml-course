import unittest

from src.graph.graph import BidirectionalGraph, BidirectionalEdge
from src.graph.mst.kruskal import kruskal_mst


class MstTest(unittest.TestCase):
    def test_kruskal(self):
        graph = BidirectionalGraph(None)

        graph.add_edge(BidirectionalEdge(0, 7, 8))
        graph.add_edge(BidirectionalEdge(0, 1, 4))
        graph.add_edge(BidirectionalEdge(1, 2, 8))
        graph.add_edge(BidirectionalEdge(1, 7, 11))
        graph.add_edge(BidirectionalEdge(2, 3, 7))
        graph.add_edge(BidirectionalEdge(2, 5, 4))
        graph.add_edge(BidirectionalEdge(3, 4, 9))
        graph.add_edge(BidirectionalEdge(3, 5, 14))
        graph.add_edge(BidirectionalEdge(5, 4, 10))
        graph.add_edge(BidirectionalEdge(6, 5, 2))
        graph.add_edge(BidirectionalEdge(7, 6, 1))
        graph.add_edge(BidirectionalEdge(7, 8, 7))
        graph.add_edge(BidirectionalEdge(8, 2, 2))
        graph.add_edge(BidirectionalEdge(8, 6, 6))

        mst = kruskal_mst(graph)
        self.assertEqual(9, len(mst.get_nodes()))
        self.assertEqual(8, len(mst.edge_list))
        self.assertEqual(37, mst.get_weight())