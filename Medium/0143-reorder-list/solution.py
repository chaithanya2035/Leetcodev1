# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        s = head
        f = head
        while f and f.next:
            s = s.next
            f = f.next.next
        
        curr = s.next
        s.next = None
        prev = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        temp = head
        temp2 = prev
        while temp and temp2:
            nxt = temp.next
            nxt2 = temp2.next
            temp.next = temp2
            temp2.next = nxt
            temp = nxt
            temp2 = nxt2

        return head
