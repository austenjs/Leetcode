# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        try:
            slow = head.next
            fast = head.next.next
        except:
            return None
        
        while fast and fast.next and slow != fast:
            slow = slow.next
            fast = fast.next.next
        
        if fast is None or fast.next is None:
            return None

        fast = head
        
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow