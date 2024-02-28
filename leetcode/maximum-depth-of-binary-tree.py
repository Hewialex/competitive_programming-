# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.maxi=0
        
        def maxd(node , count):
            if not node:
                self.maxi = max(self.maxi , count)
                return
            maxd(node.left , count+1)
            maxd(node.right , count + 1)
        maxd(root , 0)
        return self.maxi




        