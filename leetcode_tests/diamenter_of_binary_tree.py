"""
Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # add a value to each node which heights left right
        diam, height = self.diameterPlusHeightBT(root)
        return diam

    def diameterPlusHeightBT(self, root: TreeNode) -> Tuple[int, int, int]:
        if root is None:
            return 0, 0
        diam_right, height_right = self.diameterPlusHeightBT(root.right)
        diam_left, height_left = self.diameterPlusHeightBT(root.left)
        return max(height_right + height_left, diam_right, diam_left), max(height_right, height_left) + 1


if __name__ == "__main__":
    tree = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    solution = Solution()
    print(solution.diameterOfBinaryTree(tree))


