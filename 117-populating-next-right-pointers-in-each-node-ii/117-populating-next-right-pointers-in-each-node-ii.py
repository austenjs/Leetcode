"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        
        leftmost = root
        while leftmost:
            head = leftmost
            while head:
                neighbor = head.next
                while neighbor and neighbor.left is None and neighbor.right is None:
                    neighbor = neighbor.next
                # Connect left child (if any)
                if head.left is None:
                    pass
                elif head.right:
                    head.left.next = head.right
                elif neighbor and neighbor.left:
                    head.left.next = neighbor.left
                elif neighbor and neighbor.right:
                    head.left.next = neighbor.right
                
                # Connect right child (if any)
                if head.right is None:
                    pass
                elif neighbor and neighbor.left:
                    head.right.next = neighbor.left
                elif neighbor and neighbor.right:
                    head.right.next = neighbor.right
                
                head = head.next
            while leftmost:
                if leftmost.left:
                    leftmost = leftmost.left
                    break
                elif leftmost.right:
                    leftmost = leftmost.right
                    break
                leftmost = leftmost.next
        return root