from graph import WeightedGraph
import collections
import heapq

class MinQueue():
    def __init__(self):
        self.elements = List = []
    def empty(self) -> bool:
        return len(self.elements) == 0
    def put(self, item:int, priority:float):
        heapq.heappush(self.elements, (priority, item))
    def get(self):
        return heapq.heappop(self.elements)[1]

def disjkstra_shortest_path(graph: WeightedGraph, start_node):
    frontier = MinQueue()
    frontier.put(start_node, 0)
    came_from: Dict[int, int] = {start_node:None}
    cost_so_far: Dict[int, float] = {0:0.0}

    while not frontier.empty():
        current_node = frontier.get()
        for next_node in graph.neighbours(current_node):
            new_cost = cost_so_far[current_node] + graph.weight(current_node, next_node)
            if next_node not in cost_so_far or new_cost<cost_so_far[next_node]:
                cost_so_far[next_node] = new_cost
                frontier.put(next_node, new_cost) #delete from heap and update with the new cost
                came_from[next_node] = current_node
    return came_from, cost_so_far

if __name__ == "__main__":

    wg = {
        0 : {1:5, 2:6},
        1: {3:2},
        2: {3:4}
    }
    graph = WeightedGraph(wg)
    print(graph.edges())
    print(graph.neighbours(1))
    print(graph.weight(1,3))
    came_from, cost_so_far = disjkstra_shortest_path(graph, 0)
    print(came_from)
    print(cost_so_far)

