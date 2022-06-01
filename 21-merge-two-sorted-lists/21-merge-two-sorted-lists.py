# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            head = list1
            head.next = self.mergeTwoLists(list1.next, list2)
        else:
            head = list2
            head.next = self.mergeTwoLists(list1, list2.next)
        return head