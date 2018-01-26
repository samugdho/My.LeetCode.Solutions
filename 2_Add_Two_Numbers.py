# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        b = 0
        L = ListNode(0)
        cL = L
        c,c2 = l1, l2
        cn = cL
        while c != None or c2 != None or b > 0:
            v1 = 0 if c == None else c.val
            v2 = 0 if c2 == None else c2.val
            _sum = v1 + v2 + b
            b = 0 if _sum < 10 else 1
            a = _sum%10
            cL.val = a
            cL.next = ListNode(0)
            cn = cL
            cL = cL.next
            c = None if  c == None else c.next
            c2 = None if  c2 == None else c2.next
        cn.next = None
        return L