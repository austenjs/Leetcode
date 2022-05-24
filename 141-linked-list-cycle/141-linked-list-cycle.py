# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        for i in range(10000 + 1):
            if head == None:
                return False
            elif head.val == 100001:
                return True
            head.val = 100001
            head = head.next
        return True