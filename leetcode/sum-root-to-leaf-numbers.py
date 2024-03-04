# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def leaf(node, cur):
            if not node:
                return 0
            cur += str(node.val)
            if not node.left and not node.right:
                return int(cur)
            return leaf(node.left, cur) + leaf(node.right, cur)

        return leaf(root, '')
        