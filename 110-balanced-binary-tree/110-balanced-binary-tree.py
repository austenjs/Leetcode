# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return abs(self.height(root.left) - self.height(root.right)) <= 1 \
            and self.isBalanced(root.left) \
            and self.isBalanced(root.right)
        
    def height(self, node):
        if node is None:
            return 0
        if node in self.memo:
            return self.memo[node]
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        if left_height > right_height:
            height = 1 + left_height
        else:
            height = 1 + right_height
        self.memo[node] = height
        return height