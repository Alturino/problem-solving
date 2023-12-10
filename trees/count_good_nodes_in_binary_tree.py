from typing import Optional


class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(maxValue: int, node: TreeNode):
            if not node:
                return 0

            res = 1 if node.val >= maxValue else 0
            maxValue = max(maxValue, node.val)
            if node.left:
                res += dfs(maxValue, node.left)
            if node.right:
                res += dfs(maxValue, node.right)
            return res

        return dfs(root.val, root)


s = Solution()
print(
    s.goodNodes(
        root=TreeNode(
            val=9,
            left=None,
            right=TreeNode(
                val=3,
                right=TreeNode(val=6),
            ),
        )
    )
)
