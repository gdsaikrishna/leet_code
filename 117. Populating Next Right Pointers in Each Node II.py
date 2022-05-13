"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        old_root, parent = root,  Node(0)
        child = parent
        while root:
            #Chaining in Level nodes
            while root:
                if root.left:
                    child.next = root.left
                    child = child.next
                if root.right:
                    child.next = root.right
                    child = child.next
                root = root.next
            root, child = parent.next, parent
            child.next = None # Reset the chain for parent
        return old_root