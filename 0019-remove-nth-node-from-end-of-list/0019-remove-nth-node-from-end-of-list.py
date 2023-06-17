# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current=head
        length=0
        while current:
            length+=1
            current=current.next
        if length == n : return head.next
        i=1
        current=head
        while i<length-n:
            current=current.next
            i=i+1
        current.next=current.next.next
        return head