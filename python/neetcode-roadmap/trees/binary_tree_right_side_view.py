import collections
from typing import Deque, List, Optional


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
    def goodNodes(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q: Deque[TreeNode] = collections.deque([root])
        while q:
            rightSide = None

            for i in range(len(q)):
                currentNode: TreeNode = q.popleft()
                if currentNode:
                    rightSide = currentNode
                    q.append(currentNode.left)
                    q.append(currentNode.right)

            if rightSide:
                res.append(rightSide.val)

        return res


s = Solution()
print(
    s.goodNodes(
        root=TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(val=5),
            ),
            right=TreeNode(
                val=3,
                right=TreeNode(val=4),
            ),
        ),
    )
)
