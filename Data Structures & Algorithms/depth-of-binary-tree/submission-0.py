# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth1 = 0

        def dfs(root1, depth):
            depth += 1
            if root1 == None:
                return depth
            return max(dfs(root1.left, depth), dfs(root1.right, depth))
        return(dfs(root, depth1) - 1)
        


        