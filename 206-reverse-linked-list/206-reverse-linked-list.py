# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, pointer = None, head
        
        while pointer:
            tmp = pointer.next
            pointer.next = prev
            prev, pointer = pointer, tmp
        
        return prev