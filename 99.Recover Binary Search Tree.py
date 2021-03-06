# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = first = second = None
        temp = root
        stack = []
        while True:
            while temp:
                stack.append(temp)
                temp = temp.left
            if not stack:
                break
            node = stack.pop()
            if not first and prev and prev.val > node.val:
                first = prev
            if first and prev and prev.val > node.val:
                second = node
            prev = node
            temp = node.right
        first.val, second.val = second.val, first.val