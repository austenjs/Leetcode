import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, -math.inf, math.inf)
        
    def validate(self, node, lower, upper):
        if node is None:
            return True
        print(node.val, lower, upper)
        if node.val <= lower:
            return False
        if node.val >= upper:
            return False
        
        return self.validate(node.left, lower, node.val) and self.validate(node.right, node.val, upper)