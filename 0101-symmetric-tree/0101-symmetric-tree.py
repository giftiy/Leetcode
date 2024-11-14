# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        # Helper function to check if two trees are mirror images of each other
        def isMirror(t1: TreeNode, t2: TreeNode) -> bool:
            if not t1 and not t2:
                return True  # Both are None
            if not t1 or not t2:
                return False  # One is None, the other is not
            if t1.val != t2.val:
                return False  # Values don't match
            # Recursively check the subtrees
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        
        # Check if the tree is symmetric by comparing the left and right subtrees of the root
        return isMirror(root.left, root.right)
