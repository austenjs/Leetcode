# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.count = 0
        self.isUniValue(root, root.val)
        return self.count
        
    def isUniValue(self, root, val):
        if root is None:
            return True
        if not all([self.isUniValue(root.left, root.val), self.isUniValue(root.right, root.val)]):
            return False
        self.count += 1
        return root.val == val