from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.count = defaultdict(int)
        self.level_sum = defaultdict(int)

    def traverse(self, root, level):
        if root is None:
            return
        self.count[level] += 1
        self.level_sum[level] += root.val
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        self.traverse(root, 0)
        max_depth = max(self.count.keys())
        ans = []
        for level in range(max_depth + 1):
            ans.append(self.level_sum[level] / self.count[level])
        return ans