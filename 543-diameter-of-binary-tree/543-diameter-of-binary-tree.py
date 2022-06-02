# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        current = 0
        if root.left is not None:
            current += 1
        if root.right is not None:
            current += 1
        current += self.calculateDiameter(root.left) + self.calculateDiameter(root.right)
        return max(current, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    def calculateDiameter(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        left = self.calculateDiameter(root.left)
        right = self.calculateDiameter(root.right)
        return 1 + max(left, right)