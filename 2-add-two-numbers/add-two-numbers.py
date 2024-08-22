# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry=0
        l3=ListNode()
        current=l3
        while l1 or l2 or carry:
            l1_value=l1.val if l1 else 0
            l2_value=l2.val if l2 else 0
            total=l1_value+l2_value+carry
            carry=total/ 10
            current.next=ListNode(total % 10)
            current=current.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
            
        return l3.next
        
            