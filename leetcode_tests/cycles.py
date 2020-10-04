"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5
"""
from typing import List
class Solution:
    def convertEdgesToNodesList(self, numCourses, prerequisites: List[List[int]]):
        print(numCourses)
        nodes = [[] for i in range(numCourses)]
        print(nodes)
        for prer in prerequisites:
            nodes[prer[0]].append(prer[1])
        print(nodes)
        return nodes

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        print(prerequisites)
        # graph represented as adjancy list
        nodes = self.convertEdgesToNodesList(numCourses, prerequisites)

        for node in range(len(nodes)):
            visited = [0] * numCourses
            if self.visit_cycles(node, node, nodes, visited):
                return False
        return True
    def visit_cycles(self, start_node, curr_node, neighbours_list, visited):
        visited[curr_node] +=1
        for node in neighbours_list[curr_node]:
            if node == start_node:
                return True #has cycles
            else:
                if visited[node]==0:
                    cycle = self.visit_cycles(start_node, node, neighbours_list, visited)
                    if cycle:
                        return True
        return False #no cycles

if __name__ == "__main__":
    solution = Solution()
    prerequisites = [[1,0],[0,1]]
    num_courses = 2
    print(solution.canFinish(num_courses, prerequisites))
