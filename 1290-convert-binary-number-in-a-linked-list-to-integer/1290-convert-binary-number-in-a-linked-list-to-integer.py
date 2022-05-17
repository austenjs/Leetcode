# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans = 0
        power = 29
        while head:
            ans += head.val * (2 ** power)
            power -= 1
            head = head.next
        return ans // (2 ** (power + 1))