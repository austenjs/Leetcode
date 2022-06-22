# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left and root.val <= root.left.val:
            return False
        if root.right and root.val >= root.right.val:
            return False
        
        return self.validate(root.left, None, root.val) and self.validate(root.right, root.val, None)
        
    def validate(self, node, lower, upper):
        if node is None:
            return True
        if lower and node.val <= lower:
            return False
        if upper and node.val >= upper:
            return False
        
        return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)