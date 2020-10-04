from typing import Dict, List, DefaultDict
from collections import defaultdict
class Graph:
    def __init__(self, edges_dict: DefaultDict[int, List[int]]):
        self.__edges = defaultdict(list)
        self.__edges.update(edges_dict)

    def edges(self):
        return self.__edges

    def neighbours(self, node_id):
        return self.__edges[node_id]

class WeightedGraph(Graph):
    def __init__(self, edges_dict:DefaultDict[int, DefaultDict[int, float]]):
        self.__edges = defaultdict(DefaultDict)
        self.__edges.update(edges_dict)

    def edges(self):
        return self.__edges

    def neighbours(self, node_id):
        return self.__edges[node_id]

    def weight(self, node_start, node_end):
        return self.neighbours(node_start)[node_end] #the weight


if __name__ == "__main__":
    g= {
        0: [1,2],
        1: [3],
        2: [3]
    }

    graph = Graph(g)
    print(graph.edges())

    wg = {
        0 : {1:5, 2:6},
        1: {3:2},
        2: {3:4}
    }
    graph = WeightedGraph(wg)
    print(graph.edges())
    print(graph.neighbours(1))
    print(graph.weight(1,3))
