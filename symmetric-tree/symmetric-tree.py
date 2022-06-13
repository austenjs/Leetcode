# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.checkSymmetric(root.left, root.right)

    def checkSymmetric(self, node1, node2):
        if node1 is None or node2 is None:
            return node1 == node2
        if node1.val != node2.val:
            return False
        return self.checkSymmetric(node1.left, node2.right) and self.checkSymmetric(node1.right, node2.left)