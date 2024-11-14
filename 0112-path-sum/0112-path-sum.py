# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: TreeNode, target: int) -> bool:
        # Base case: if the tree is empty
        if not root:
            return False
        
        # If we've reached a leaf node, check if the sum matches the target
        if not root.left and not root.right:
            return target == root.val
        
        # Recursively check the left and right subtrees with the reduced target
        target -= root.val
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)
