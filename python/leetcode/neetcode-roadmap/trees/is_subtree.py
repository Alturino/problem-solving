from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)


s = Solution()
root = TreeNode(
    3,
    left=TreeNode(4, left=TreeNode(1), right=TreeNode(2, left=TreeNode(0))),
    right=TreeNode(5),
)
subRoot = TreeNode(4, left=TreeNode(1), right=TreeNode(2))
print(s.isSubtree(root, subRoot))