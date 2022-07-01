# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lst = []
        N = 0
        while head:
            lst.append(head)
            N += 1
            head = head.next
        lst.append(None)
        idx = N - n
        if idx == 0:
            return lst[1]
        elif idx == N - 1:
            lst[-3].next = None
        else:
            lst[idx - 1].next = lst[idx + 1]
        return lst[0]
        
        
        