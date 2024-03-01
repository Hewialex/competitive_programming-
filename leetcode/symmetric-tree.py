# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        arr1 = []
        arr2 = []
        def preorder1(node):
            if not node:
                arr1.append(None)
                return
            arr1.append(node.val)
            preorder1(node.left)
            preorder1(node.right)
        def preorder2(node):
            if not node:
                arr2.append(node)
                return
            arr2.append(node.val)
            preorder2(node.right)
            preorder2(node.left)
        preorder1(root)
        preorder2(root)
        
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                return False
        return True
            
            