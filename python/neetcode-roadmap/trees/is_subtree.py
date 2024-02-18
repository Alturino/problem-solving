from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not t:
            return True
        if not s:
            return False

        if self.sameTree(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if s and t and s.val == t.val:
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False


s = Solution()
root = TreeNode(
    3,
    left=TreeNode(4, left=TreeNode(1), right=TreeNode(2, left=TreeNode(0))),
    right=TreeNode(5),
)
subRoot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
print(s.isSubtree(root, subRoot))
