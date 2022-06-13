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
        _ = self.isUnival(root, root.val)
        return self.count
        
    def isUnival(self, root, val):
        if root is None:
            return True
        left = self.isUnival(root.left, root.val)
        right = self.isUnival(root.right, root.val)
        if not (left and right):
            return False
        self.count += 1 # Unival
        return root.val == val