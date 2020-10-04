from graph import WeightedGraph
from dijkstra import MinQueue
def heuristic(node1, node2):
    if node1 == node2:
        return 0
    else:
        return 1
def a_star_search(graph: WeightedGraph, start_node: int, end_node: int):
    frontier = MinQueue()
    frontier.put(start_node, 0)
    cost_so_far = {start_node:0}
    come_from = {start_node:None}
    while not frontier.empty():
        current_node = frontier.get()
        if current_node == end_node:
            break
        for neighbor in graph.neighbours(current_node):
            new_cost = cost_so_far[current_node] + graph.weight(current_node, neighbor)
            if neighbor not in cost_so_far or cost_so_far[neighbor] > new_cost:
                cost_so_far[neighbor] = new_cost
                frontier.put(neighbor, new_cost + heuristic(current_node, neighbor))
                come_from[neighbor] = current_node
    return come_from, cost_so_far

if __name__ == "__main__":
    wg = {
        0: {1: 5, 2: 6},
        1: {3: 2},
        2: {3: 4}
    }
    graph = WeightedGraph(wg)
    come_from, cost_so_far = a_star_search(graph, 0, 3)
    print(come_from)
    print(cost_so_far)