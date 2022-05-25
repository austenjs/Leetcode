# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        tmp = []
        while head:
            tmp.append(head.val)
            head = head.next
        left, right = 0, len(tmp) - 1
        while left < right:
            if tmp[left] != tmp[right]:
                return False
            left += 1
            right -= 1
        return True