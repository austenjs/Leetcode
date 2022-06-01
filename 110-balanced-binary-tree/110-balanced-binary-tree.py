# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _ = self.height(root)
        return self.ans
        
    def height(self, node):
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if left_height > right_height:
            height = 1 + left_height
        else:
            height = 1 + right_height
        if left_height - right_height > 1 or right_height - left_height > 1:
            self.ans = False
        return height