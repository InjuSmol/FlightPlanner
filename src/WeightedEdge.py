class WeightedEdge:
    def __init__(self, init_node1: str, init_node2: str, init_weight: float):
        self.node1 = init_node1
        self.node2 = init_node2
        self.weight = init_weight
    
    def get_node1(self) -> str:
        return self.node1
    
    def get_node2(self) -> str:
        return self.node2
    
    def get_weight(self) -> float:
        return self.weight
