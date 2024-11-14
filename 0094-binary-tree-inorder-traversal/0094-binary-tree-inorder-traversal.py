# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        # Initialize result list
        result = []
        
        # Helper function to perform inorder traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)  # Traverse left subtree
            result.append(node.val)  # Visit current node
            inorder(node.right)  # Traverse right subtree
        
        inorder(root)
        return result
