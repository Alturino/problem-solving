import collections
from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node: Optional[TreeNode], left, right):
            if not node:
                return True

            if not (left < node.val < right):
                return False

            return isValid(
                node.left,
                left,
                node.val,
            ) and isValid(
                node.right,
                node.val,
                right,
            )

        return isValid(root, float("-inf"), float("inf"))


s = Solution()
print(
    s.isValidBST(
        root=TreeNode(
            val=2,
            left=TreeNode(val=1),
            right=TreeNode(val=3),
        )
    )
)
print(
    s.isValidBST(
        root=TreeNode(
            val=5,
            left=TreeNode(val=1),
            right=TreeNode(
                val=4,
                left=TreeNode(val=3),
                right=TreeNode(val=6),
            ),
        )
    )
)
