# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(node):
            if not node:
                return []

            left = inorder(node.left)
            current = [node.val]
            right = inorder(node.right)

            return left + current + right

        inorderT = inorder(root)

        for i in range(1, len(inorderT)):
            if inorderT[i] <= inorderT[i - 1]:
                return False

        return True