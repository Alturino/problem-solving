from re import T
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findHeight(node: Optional[TreeNode] = root) -> int:
            if not node:
                return 0

            left = 1 + findHeight(node.left)
            right = 1 + findHeight(node.right)
            return abs(left - right)

        diff = findHeight(root)
        print(diff)
        return diff in range(0, 1)
