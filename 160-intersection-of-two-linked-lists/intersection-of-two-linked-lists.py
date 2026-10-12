# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        x=headA
        y=headB
        while x!=y:
            if x is None:
                x=headB
            else:
                x=x.next
            if y is None:
                y=headA
            else:
                y=y.next
        return y
        