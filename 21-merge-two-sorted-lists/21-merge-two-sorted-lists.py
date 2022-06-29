# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            new_head = list2
            new_head.next = self.mergeTwoLists(list1, list2.next)
        else:
            new_head = list1
            new_head.next = self.mergeTwoLists(list1.next, list2)
        return new_head