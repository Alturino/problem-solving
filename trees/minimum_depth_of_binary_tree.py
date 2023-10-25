from typing import Optional

class TreeNode:
    def __init__(self, val=0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)
        if root.left is None:
            return 1 + rightDepth
        if root.right is None:
            return 1 + leftDepth
        
        return min(leftDepth, rightDepth) + 1

s = Solution()
# t = TreeNode(val=2, right=TreeNode(val=3, right=TreeNode(val=4, right=TreeNode(val=5, right=TreeNode(val=6)))))
t = TreeNode(val = 3, left=TreeNode(val = 9), right=TreeNode(val = 20, left=TreeNode(15), right=TreeNode(7)),)
print(s.minDepth(root=t))
