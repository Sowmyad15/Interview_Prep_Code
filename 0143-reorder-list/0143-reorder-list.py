# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        [1,2,3,4,5,6,7]-->[1,7,2,6,3,5,4]-->[1,2,3,4],[7,6,5]
        1-->finding the mid
        2-->swap right subarray after mid
        3-->Merge
        """
        fast=slow=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        
        prev,current=None,slow.next
        while current:
            new=current.next
            current.next=prev
            prev=current
            current=new
        slow.next=None

        head1,head2=head,prev
        while head2:
            new=head1.next
            head1.next=head2
            head1=head2
            head2=new
        


