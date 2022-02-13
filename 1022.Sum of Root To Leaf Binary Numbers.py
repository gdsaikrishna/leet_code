# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.sum_total = 0
        if not root:
            return self.sum_total
        def helper(node, path):
            if node.left is None and node.right is None:
                self.sum_total += path
                
            if node.left:
                helper(node.left, path*2 + node.left.val)
            if node.right:
                helper(node.right, path*2 + node.right.val)
        
        helper(root, root.val)
        return self.sum_total