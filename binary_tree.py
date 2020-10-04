import math

"""
The encoding of the binary tree is using an array as follows
bt_tree = [0,
           1, 2,
           3, None, None, None,
           7, 8, None, None, None, None, None, None, 
           None, None, 17]
"""


def parent(index):
    return (index - 1) // 2


def level(index):
    return math.trunc(math.log2(index + 1))


def find_common_ancestor(index1, index2):
    # indexes based solution
    if index2 < index1:
        index1, index2 = index2, index1

    # get to the same level
    while level(index2) > level(index1):
        index2 = parent(index2)

    while index1 != index2:  # (index1>0) and
        index1 = parent(index1)
        index2 = parent(index2)
    return index1


if __name__ == "__main__":
    # possible edge case
    index1 = 0
    index2 = 1
    common_ancestor = find_common_ancestor(index1, index2)
    print(f"Index of common ancestor of indexes {index1} and {index2} is {common_ancestor}")

    # find common ancestor of element at index 7 and 4
    index1 = 7
    index2 = 4
    common_ancestor = find_common_ancestor(index1, index2)
    print(f"Index of common ancestor of indexes {index1} and {index2} is {common_ancestor}")

    # wiki example - tree not needed, just included to see the structure of the underlying array
    bt_tree = [0, 1, 2, 3, None, None, None, 7, 8, None, None, None, None, None, None, None, None, 17]
    print(f"Wiki example : {bt_tree}")
    index1 = 7
    index2 = 17
    common_ancestor = find_common_ancestor(index1, index2)
    print(f"Index of common ancestor of indexes {index1} and {index2} is {common_ancestor}")
    print(f"Common ancestor value {bt_tree[common_ancestor]}")