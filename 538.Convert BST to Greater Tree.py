# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0
        return self.reverse_inorder(root)
    def reverse_inorder(self, root):
        if not root: return
        self.reverse_inorder(root.right)
        self.sum += root.val
        root.val = self.sum
        self.reverse_inorder(root.left)
        return root