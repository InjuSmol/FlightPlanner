from WeightedEdge import WeightedEdge
from typing import List
import math

class WeightedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def get_keys(self, keys: List[str]) -> None:
        testKeys = list(self.nodes.keys())
        keys.extend(testKeys)

    def node_exists(self, testNode: str) -> bool:
        return testNode in self.nodes

    def get_edge_id(self, node1: str, node2: str) -> str:
        return node1 + "-" + node2

    def add_node(self, nodeId: str, nodeData: any) -> None:
        self.nodes[nodeId] = nodeData

    def getNodeData(self, nodeId: str) -> any:
        return self.nodes.get(nodeId)

    def addEdge(self, node1: str, node2: str, weight: float) -> None:
        edgeId = self.getEdgeId(node1, node2)
        self.edges[edgeId] = WeightedEdge(node1, node2, weight)

    def removeEdge(self, node1: str, node2: str) -> None:
        edgeId = self.getEdgeId(node1, node2)
        self.edges.pop(edgeId, None)

    def getNeighbors(self, neighbors: List[str], node: str) -> None:
        testKeys = list(self.edges.keys())
        for key in testKeys:
            index = key.index("-")
            startNode = key[:index]
            if startNode == node:
                neighbor = key[index + 1:]
                neighbors.append(neighbor)

    def areNeighbors(self, node1: str, node2: str) -> bool:
        neighbors = []
        self.getNeighbors(neighbors, node1)
        return node2 in neighbors

    def getNeighborWeight(self, node1: str, node2: str) -> int:
        if self.areNeighbors(node1, node2):
            edgeId = self.getEdgeId(node1, node2)
            return self.edges[edgeId].getWeight()
        return 0

    def findPath(self, path: List[str], node1: str, node2: str) -> None:
        print("Finding path from " + node1 + " to " + node2 + "\n")

        if node1 not in self.nodes or node2 not in self.nodes:
            return

        path.append(node1)

        visited = {node1: node1}

        while path:
            last = path[-1]

            neighbors = []
            self.getNeighbors(neighbors, last)

            closestIndex = -1
            closestDistance = math.inf
            for i, testNeighbor in enumerate(neighbors):
                if testNeighbor == node2:
                    path.append(testNeighbor)
                    return

                if testNeighbor not in visited:
                    id = self.getEdgeId(last, testNeighbor)
                    edge = self.edges[id]
                    if edge.getWeight() < closestDistance:
                        closestIndex = i
                        closestDistance = edge.getWeight()

            if closestIndex >= 0:
                closestNode = neighbors[closestIndex]
                visited[closestNode] = closestNode
                path.append(closestNode)
            elif path:
                path.pop()
