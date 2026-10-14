# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """

        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        s=f=head
        while f.next and f.next.next:
            s=s.next
            f=f.next.next
        c,p=s.next,None
        s.next=None
        while c:
            t=c.next
            c.next=p
            p=c
            c=t
        a,b=head, p
        while b:
            t=b.next
            b.next=a.next
            a.next=b
            a=b.next
            b=t