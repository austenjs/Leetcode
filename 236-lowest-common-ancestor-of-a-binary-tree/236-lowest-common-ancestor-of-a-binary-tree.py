# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        adj_list = {} # child-parent
        queue = deque([(None, root)])
        while queue:
            parent, cur = queue.popleft()
            adj_list[cur] = parent
            if cur.left:
                queue.append((cur, cur.left))
            if cur.right:
                queue.append((cur, cur.right))
        
        visited_by_p = set()
        cur = p
        while cur:
            visited_by_p.add(cur)
            cur = adj_list[cur]

        while q:
            if q in visited_by_p:
                return q
            q = adj_list[q]
        return None