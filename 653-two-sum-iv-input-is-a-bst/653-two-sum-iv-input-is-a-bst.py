# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        self.populate(root, seen)
        
        for num in seen:
            complement = k - num
            if complement != num and complement in seen:
                return True
        return False
        
        
    def populate(self, root, visited):
        if root is None:
            return
        visited.add(root.val)
        self.populate(root.left, visited)
        self.populate(root.right, visited)