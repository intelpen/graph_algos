"""
The binary tree is defined as discussed previously only with nodes with link to parent
"""


class BTNode:
    def __init__(self, node_value, parent):
        self.node_value = node_value
        self.parent = parent
        self.visited = False


def find_common_ancestor(node1, node2):
    # visit node 1 parents
    while node1 is not None:
        node1.visited = True
        node1 = node1.parent
    # visit parents of node 2
    while node1 is not None and node2.visited is False:  # "node1 is not None" is kind of defensive programming, if the tree is illformed (node2 is from another tree)
        node2 = node2.parent

    return node2


if __name__ == "__main__":
    # possible edge case, tree with root and one leaf
    # create tree
    root_node = BTNode(0, None)
    node1 = BTNode(1, root_node)
    # find common ancestor
    common_ancestor = find_common_ancestor(node1, root_node)
    print(f"Index of common ancestor of {node1.node_value} and {root_node.node_value} is {common_ancestor.node_value}")

    # find common ancestor of element at index 7 and 4
    # create test tree
    root_node = BTNode(0, None)
    node1 = BTNode(1, root_node)
    node4 = BTNode(4, node1)
    node7 = BTNode(7, BTNode(3, node1))
    # find common ancestor
    common_ancestor = find_common_ancestor(node4, node7)
    print(f"Index of common ancestor of {node4.node_value} and {node7.node_value} is {common_ancestor.node_value}")
