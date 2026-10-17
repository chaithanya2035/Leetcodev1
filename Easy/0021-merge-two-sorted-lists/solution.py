# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy_head = dummy
        l1 = list1
        l2 = list2
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                dummy.next = l1
                dummy = dummy.next
                l1 = l1.next
            elif l2.val < l1.val:
                dummy.next = l2
                dummy = dummy.next
                l2 = l2.next

        dummy.next = l1 if l1 else l2

        return dummy_head.next
