# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        height = self.get_height(root)
        queue = deque([root])
        ans = []
        for _ in range(height):
            new_queue = deque()
            last = None
            while queue:
                cur = queue.popleft()
                if cur is None:
                    continue
                last = cur
                new_queue.append(cur.left)
                new_queue.append(cur.right)
            queue = new_queue
            if last is None:
                continue
            ans.append(last.val)
        return ans
            
    def get_height(self, root):
        if root is None:
            return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return 1 + max(left, right)