class WeightedEdge:
    def __init__(self, initNode1: str, initNode2: str, initWeight: float):
        self.node1 = initNode1
        self.node2 = initNode2
        self.weight = initWeight
    
    def getNode1(self) -> str:
        return self.node1
    
    def getNode2(self) -> str:
        return self.node2
    
    def getWeight(self) -> float:
        return self.weight
