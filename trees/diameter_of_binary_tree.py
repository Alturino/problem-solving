from typing import Optional

class TreeNode:
    def __init__(self, val:int = 0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(root: Optional[TreeNode]):
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res[0] = max(res[0], 2 + left + right)
            return 1 + max(left, right)
        dfs(root)
        return res[0]
s = Solution()
t = TreeNode(1, left=TreeNode(2, left=TreeNode(4), right=TreeNode(5)), right=TreeNode(3))
# t = TreeNode(1, left=TreeNode(2))
print(s.diameterOfBinaryTree(root=t))
