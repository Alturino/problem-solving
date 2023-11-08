from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


s = Solution()
# p = TreeNode(1 ,left=TreeNode(2))
# q = TreeNode(1 ,right=TreeNode(2))
p = TreeNode(1, right=TreeNode(3), left=TreeNode(2))
q = TreeNode(1, right=TreeNode(3), left=TreeNode(2))
print(s.isSameTree(p, q))
