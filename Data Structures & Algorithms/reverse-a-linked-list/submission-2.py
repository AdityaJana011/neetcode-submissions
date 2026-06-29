# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #base case: if head->None, return none
        if not head:
            return None
        
        newHead = head      # initially
        if head.next:       #list of more than one element
            #sub-problem exists to be reversed
            newHead = self.reverseList(head.next)       # passing the subproblem from the next element after head
            # the function returns the last element as the newHead after reversing
            #every later call returns the newHead from the deepest call, so newHead never changes after the base case
            head.next.next = head   # reversing the list for the smallest 1 element subproblem
            #creates a cycle
        head.next = None    #setting the 1st pointer to null, already true for 1st call

        return newHead