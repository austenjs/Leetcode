# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return root == subRoot
        if root.val == subRoot.val and self.checkDescendant(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    def checkDescendant(self, root, subRoot):
        if root is None or subRoot is None:
            return root == subRoot
        if root.val != subRoot.val:
            return False
        return self.checkDescendant(root.left, subRoot.left) and self.checkDescendant(root.right, subRoot.right)