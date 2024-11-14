# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # Helper function to calculate the height and check balance
        def check_balance(node):
            if not node:
                return 0  # Base case: height of empty tree is 0
            
            # Recursively check left and right subtree heights
            left_height = check_balance(node.left)
            if left_height == -1:  # If the left subtree is unbalanced, return -1
                return -1
            
            right_height = check_balance(node.right)
            if right_height == -1:  # If the right subtree is unbalanced, return -1
                return -1
            
            # If the current node is unbalanced, return -1
            if abs(left_height - right_height) > 1:
                return -1
            
            # Return the height of the current node
            return max(left_height, right_height) + 1
        
        # Start checking balance from the root
        return check_balance(root) != -1
