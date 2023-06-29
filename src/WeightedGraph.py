from WeightedEdge import WeightedEdge
from typing import List
import math


class WeightedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def get_keys(self, keys: List[str]) -> None:
        test_keys = list(self.nodes.keys())
        keys.extend(test_keys)

    def node_exists(self, test_node: str) -> bool:
        return test_node in self.nodes

    def get_edge_id(self, node1: str, node2: str) -> str:
        return node1 + "-" + node2

    def add_node(self, node_id: str, node_data: any) -> None:
        self.nodes[node_id] = node_data

    def get_node_data(self, node_id: str) -> any:
        return self.nodes.get(node_id)

    def add_edge(self, node1: str, node2: str, weight: float) -> None:
        edge_id = self.get_edge_id(node1, node2)
        self.edges[edge_id] = WeightedEdge(node1, node2, weight)

    def remove_edge(self, node1: str, node2: str) -> None:
        edge_id = self.get_edge_id(node1, node2)
        self.edges.pop(edge_id, None)

    def get_neighbors(self, neighbors: List[str], node: str) -> None:
        test_keys = list(self.edges.keys())
        for key in test_keys:
            index = key.index("-")
            start_node = key[:index]
            if start_node == node:
                neighbor = key[index + 1:]
                neighbors.append(neighbor)

    def are_neighbors(self, node1: str, node2: str) -> bool:
        neighbors = []
        self.get_neighbors(neighbors, node1)
        return node2 in neighbors

    def get_neighbor_weight(self, node1: str, node2: str) -> int:
        if self.are_neighbors(node1, node2):
            edge_id = self.get_edge_id(node1, node2)
            return self.edges[edge_id].get_weight()
        return 0

    def find_path(self, path: List[str], node1: str, node2: str) -> None:
        print("Finding path from " + node1 + " to " + node2 + "\n")

        if node1 not in self.nodes or node2 not in self.nodes:
            return

        path.append(node1)

        visited = {node1: node1}

        while path:
            last = path[-1]

            neighbors = []
            self.get_neighbors(neighbors, last)

            closest_index = -1
            closest_distance = math.inf
            for i, test_neighbor in enumerate(neighbors):
                if test_neighbor == node2:
                    path.append(test_neighbor)
                    return

                if test_neighbor not in visited:
                    id1 = self.get_edge_id(last, test_neighbor)
                    edge = self.edges[id1]
                    if edge.get_weight() < closest_distance:
                        closest_index = i
                        closest_distance = edge.getWeight()

            if closest_index >= 0:
                closest_node = neighbors[closest_index]
                visited[closest_node] = closest_node
                path.append(closest_node)
            elif path:
                path.pop()
