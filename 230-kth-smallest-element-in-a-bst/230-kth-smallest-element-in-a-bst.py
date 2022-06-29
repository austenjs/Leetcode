# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        pos = self.rank(root.left) + 1
        if pos == k:
            return root.val
        elif pos < k:
            return self.kthSmallest(root.right, k - pos)
        else:
            return self.kthSmallest(root.left, k)
    
    def rank(self, root):
        if root is None:
            return 0
        if root.left is None:
            return self.rank(root.right) + 1
        if root.right is None:
            return self.rank(root.left) + 1
        return 1 + self.rank(root.left) + self.rank(root.right)