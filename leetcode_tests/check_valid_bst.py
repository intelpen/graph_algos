# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidHeap(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if root.left.val >= root.val or self.isValidBST(root.left) is False:
                return False
        if root.right is not None:
            if root.right.val <= root.val or self.isValidBST(root.right) is False:
                return False
        return True

    def isValidBSTMinMax(self, root: TreeNode) -> Tuple[bool, int, int]:
        if root is None:
            return True, None, None
        min_left, max_left, min_right, max_right = None, None, None, None
        if root.left is not None:
            valid_left, min_left, max_left = self.isValidBSTMinMax(root.left)
            if valid_left is False:
                return False, None, None
            elif max_left >= root.val:
                return False, None, None
        else:
            min_left = root.val
        if root.right is not None:
            valid_right, min_right, max_right = self.isValidBSTMinMax(root.right)
            if valid_right is False:
                return False, None, None
            elif min_right <= root.val:
                return False, None, None
        else:
            max_right = root.val
        return True, min_left, max_right

    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        valid, min_left, max_right = self.isValidBSTMinMax(root)
        return valid


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    solution = Solution()
    print(solution.isValidBST(root))





