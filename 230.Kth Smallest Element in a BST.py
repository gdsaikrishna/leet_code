# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stac = collections.deque(maxlen=k)
        while True:
            while root:
                stac.append(root)
                root = root.left
            root = stac.pop()
            if k == 1:
                return root.val
            k -= 1
            root = root.right