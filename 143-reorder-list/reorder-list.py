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
        arr=[]
        while head:
            arr.append(head)
            head=head.next
        l,r=0,len(arr)-1
        while l<r:
            arr[l].next=arr[r]
            l+=1
            if l==r:
                break
            arr[r].next=arr[l]
            r -=1
        arr[l].next = None