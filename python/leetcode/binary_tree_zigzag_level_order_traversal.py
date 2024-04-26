from typing import Optional
import collections
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = collections.deque([root])
        level = 1
        while q:
            currLevelNodes = []
            for i in range(len(q)):
                if level % 2 == 1:
                    node = q.pop()
                    currLevelNodes.append(node.val)
                    if node.left:
                        q.appendleft(node.left)
                    if node.right:
                        q.appendleft(node.right)
                else:
                    node = q.popleft()
                    currLevelNodes.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
            res.append(currLevelNodes.copy())
            level += 1

        return res


s = Solution()
# print(
#     s.zigzagLevelOrder(
#         root=TreeNode(
#             val=3,
#             left=TreeNode(val=9),
#             right=TreeNode(
#                 val=20,
#                 left=TreeNode(val=15),
#                 right=TreeNode(val=7),
#             ),
#         )
#     )
# )
print(
    s.zigzagLevelOrder(
        root=TreeNode(
            val=1,
            left=TreeNode(
                val=2,
                left=TreeNode(val=4),
            ),
            right=TreeNode(
                val=3,
                right=TreeNode(val=5),
            ),
        )
    )
)
