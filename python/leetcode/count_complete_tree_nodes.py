from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # def countNodes(self, root: Optional[TreeNode]) -> int:
    #     def dfs(node: Optional[TreeNode]) -> int:
    #         if not node:
    #             return 0
    #
    #         return 1 + dfs(node.left) + dfs(node.right)
    #
    #     return dfs(root)

    def countNodes(self, root: Optional[TreeNode]) -> int:
        leftHeight = rightHeight = 0
        curr = root
        while curr:
            leftHeight += 1
            curr = curr.left

        curr = root
        while curr:
            rightHeight += 1
            curr = curr.right

        if leftHeight == rightHeight:
            return (1 << leftHeight) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
