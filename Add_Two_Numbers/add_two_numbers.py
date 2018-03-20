# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c=0
        begin = ListNode(0)
        current = begin
        while l1 or l2:
            if l1 == None:
                x = 0
            else:
                x = l1.val
            if l2 == None:
                y = 0
            else:
                y = l2.val
            s = x+y+c
            result = (s)%10
            if s >= 10:
                c=1
            else:
                c=0
            current.next = ListNode(result)
            current = current.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        if c==1:
            new = ListNode(1)
            current.next = new
        return begin.next
            
            
        
