# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(node, value):
            if not node or node.val == value:
                return node

            if node.val > value:
                return search(node.left, value)
            else:
                return search(node.right, value)

        return search(root, val)