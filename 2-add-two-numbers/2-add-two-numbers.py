# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        first_number = 0
        power = 0
        while l1:
            first_number += l1.val * (10 ** power)
            power += 1
            l1 = l1.next
        second_number = 0
        power = 0
        while l2:
            second_number += l2.val * (10 ** power)
            power += 1
            l2 = l2.next
        total = first_number + second_number
        head = ListNode(total % 10)
        total //= 10
        current = head
        while total != 0:
            new_node = ListNode(total % 10)
            current.next = new_node
            total //= 10
            current = new_node
        return head