from typing import Optional

class TreeNode:
    def __init__(self, val=0,left=None,right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]):
    #     if not root:
    #         return 0
    #     
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    
    # def maxDepth(self, root: Optional[TreeNode]):
    #     if not root:
    #         return 0
    #
    #     level = 0
    #     q = deque([root])
    #     while q:
    #         for i in range(len(q)):
    #             node = q.popleft() 
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #         level += 1
    #     return level

    def maxDepth(self, root: Optional[TreeNode]):
        st = [[root, 1]]
        res = 0
        while st:
            node, depth = st.pop()
            if node:
                res = max(res, depth)
                st.append([node.left, depth + 1])
                st.append([node.right, depth + 1])
        return res
s = Solution()
t = TreeNode(val = 3, left=TreeNode(val = 9), right=TreeNode(val = 20, left= TreeNode(val = 15), right=TreeNode(val = 7)))
print(s.maxDepth(root=t))
