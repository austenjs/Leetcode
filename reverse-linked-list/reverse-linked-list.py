# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.reverse(head)[0]
        
    def reverse(self, head):
        if head is None or head.next is None:
            return head, head
        end = head
        new_head, new_tail = self.reverse(head.next)
        end.next = None
        if new_tail:
            new_tail.next = end
        else:
            new_tail = end
        
        return new_head, end