# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if (head==None):
            return head 
        dummy=ListNode(0)
        dummy.next=head
        temp=head
        prev=dummy
        while(temp and temp.next!=None):
            temp1=temp.next
            if (temp1.val==temp.val):
                while (temp and temp.val==temp1.val):
                    temp=temp.next
                prev.next = temp
            else:
                prev=temp
                temp=temp.next
        return dummy.next
