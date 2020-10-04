from graph import Graph
from typing import Dict, List, DefaultDict
import collections
from collections import defaultdict


def breadth_first_search(graph: Graph, start_node: int):
    frontier = collections.deque()
    frontier.append(start_node)
    visited: Dict[int, bool] = {start_node: True}

    while len(frontier) != 0:
        current = frontier.popleft()

        print(current)
        for node in graph.neighbours(current):
            if node not in visited:
                visited[node] = True
                frontier.append(node)



def breadth_first_search_edges(edges: DefaultDict[int, List[int]], start_node: int):
    frontier = collections.deque()
    frontier.append(start_node)
    visited: Dict[int] = {}  # list [0] * n works also
    visited[start_node] = True
    while len(frontier) != 0:
        current = frontier.popleft()

        print(current)
        for node in edges[current]:
            if node not in visited:
                visited[node] = True
                frontier.append(node)

def breadth_first_search_with_dest(graph: Graph, start_node, end_node):
    frontier = collections.deque()
    frontier.append(start_node)
    came_from : Dict[int] = {start_node: None}
    while len(frontier) != 0:
        current = frontier.popleft()
        if current == end_node:
            break
        for node in graph.neighbours(current):
            if node not in came_from:
                came_from[node] = current
                frontier.append(node)
    return came_from

if __name__ == "__main__":

    g = defaultdict(list)
    g.update({
        0: [1, 2],
        1: [3],
        2: [3],
    })
    print("Test BFS")
    graph = Graph(g)
    breadth_first_search(graph, 0)
    breadth_first_search_edges(g, 0)
    print("Test BFS with start_stop")
    graph_paths = breadth_first_search_with_dest(graph, 0, 3)
    print(graph_paths)