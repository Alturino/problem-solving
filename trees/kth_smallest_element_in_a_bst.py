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
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     q = collections.deque()
    #
    #     def dfs(node: Optional[TreeNode]):
    #         if not node:
    #             return
    #
    #         dfs(node.left)
    #         q.append(node.val)
    #         dfs(node.right)
    #
    #     dfs(root)
    #     for i in range(k - 1):
    #         q.popleft()
    #     return q.popleft()

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        st = []
        curr = root

        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            curr = st.pop()
            k -= 1
            if k == 0:
                return curr.val
            curr = curr.right

        return 0


s = Solution()
print(
    s.kthSmallest(
        root=TreeNode(
            val=3,
            left=TreeNode(
                val=1,
                right=TreeNode(val=2),
            ),
            right=TreeNode(val=4),
        ),
        k=1,
    )
)
