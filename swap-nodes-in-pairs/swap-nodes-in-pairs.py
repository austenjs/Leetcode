# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        third_to_end = head.next.next
        tmp = head.next
        
        head, tmp = tmp, head
        head.next = tmp
        tmp.next = self.swapPairs(third_to_end)
        return head