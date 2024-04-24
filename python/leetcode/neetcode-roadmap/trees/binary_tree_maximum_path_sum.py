from typing import Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left=None,
        right=None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val if root else 0

        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            nonlocal res

            res = max(res, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        dfs(root)

        return res


s = Solution()
# print(
#     s.maxPathSum(
#         root=TreeNode(
#             val=1,
#             left=TreeNode(val=2),
#             right=TreeNode(val=3),
#         )
#     )
# )
print(
    s.maxPathSum(
        root=TreeNode(
            val=-10,
            left=TreeNode(val=9),
            right=TreeNode(
                val=20,
                left=TreeNode(val=15),
                right=TreeNode(val=7),
            ),
        )
    )
)
