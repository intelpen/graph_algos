from typing import List
class Solution:
    # this is a DAG, so topological ordering is possible
    def convertEdgesToNodesList(self, numCourses, prerequisites: List[List[int]]):
        #print(numCourses)
        nodes = [[] for i in range(numCourses)]
        for prer in prerequisites:
            nodes[prer[1]].append(prer[0])
        #print(nodes)
        return nodes

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodes_list = self.convertEdgesToNodesList(numCourses, prerequisites)
        n = [numCourses]
        f = [None] * numCourses
        visited = [0] * numCourses
        for node in range(numCourses):
            if visited[node] == 0:
                self.dFS(node, nodes_list, visited, n, f)
        return f

    def dFS(self, start_node, nodes_list: List[List[int]], visited: List[int], n: int, f):
        visited[start_node] = 1
        for node in nodes_list[start_node]:
            if visited[node] == 0:
                self.dFS(node, nodes_list, visited, n, f)
        f[start_node] = n[0]
        #print(f)
        n[0] -= 1


if __name__ == "__main__":
    solution = Solution()
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]
    print(solution.findOrder(numCourses, prerequisites))




