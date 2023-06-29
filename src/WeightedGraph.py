from WeightedEdge import WeightedEdge
from typing import List
from collections import deque


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

    def find_path(self, path, node1, node2):
        print(f"Finding path from {node1} to {node2}")

        if not self.node_exists(node1) or not self.node_exists(node2):
            return

        path.append(node1)
        visited = {node1}

        direct_edge_id = self.get_edge_id(node1, node2)
        direct_edge = self.edges.get(direct_edge_id)
        if direct_edge:
            path.append(node2)
            return

        distances = {node: float('inf') for node in self.nodes}
        distances[node1] = 0
        previous = {}

        queue = deque()
        queue.append(node1)

        while queue:
            current = queue.popleft()
            current_distance = distances[current]
            if current == node2:
                self.path_h(previous, node1, node2, path)
                return

            neighbors = list()
            self.get_neighbors(neighbors, current)

            for neighbor in neighbors:
                edge_id = self.get_edge_id(current, neighbor)
                weight = self.edges[edge_id].get_weight()
                distance_to_neighbor = current_distance + weight

                if distance_to_neighbor < distances[neighbor]:
                    distances[neighbor] = distance_to_neighbor
                    previous[neighbor] = current
                    visited.add(neighbor)
                    queue.append(neighbor)

    def path_h(self, previous1, start, end, path2):
        current = end
        leg_path = []
        while current != start:
            leg_path.insert(0, current)
            current = previous1[current]
        path2.extend(leg_path)



