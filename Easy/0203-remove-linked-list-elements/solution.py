# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        temp = head
        prev = None
        while temp:
            if temp.val == val:
                if prev is None:
                    head = temp.next
                else:
                    prev.next = temp.next
            else:
                prev = temp
            temp = temp.next
        return head
