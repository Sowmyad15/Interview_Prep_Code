# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        lst=[]
        for i in lists:
            while i:
                lst.append(i.val)
                i=i.next
        lst.sort()
        head=ListNode(0)
        current=head
        for i in lst:
            current.next=ListNode(i)
            current=current.next
        
        return head.next
