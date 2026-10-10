# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # find the middle
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second linked list

        second = slow.next
        slow.next = None
        prev = None

        while second:
            next_node = second.next

            second.next = prev

            prev = second
            second = next_node

        # take one at a time and add
        first = head
        second = prev

        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        