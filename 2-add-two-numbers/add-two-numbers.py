# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        d=ListNode(0)
        c=d
        x=0
        while l1 or l2 or x:
            a=l1.val if l1 else 0
            b=l2.val if l2 else 0
            s=a+b+x
            x=s//10
            c.next=ListNode(s%10)
            c=c.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return d.next