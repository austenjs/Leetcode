# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = self.getLevel(root)
        ans = [[] for _ in range(level)]
        self.populate(root, 0, ans)
        return ans
    
    def populate(self, node, level, ans):
        if node is None:
            return
        ans[level].append(node.val)
        self.populate(node.left, level + 1, ans)
        self.populate(node.right, level + 1, ans)
        
    def getLevel(self, root):
        if root is None:
            return 0
        left, right = self.getLevel(root.left), self.getLevel(root.right)
        return 1 + left if left > right else 1 + right