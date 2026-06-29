# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next     # stores where curr points as it will be lost
            curr.next = prev    # reversing the pointer of curr to look back
            prev = curr         # shifting prev to point to curr(next node)
            curr = nxt          # shifting curr to the nect node
        return prev     # after the loop, curr points to none and prev points to the last element on the list which is now the new head