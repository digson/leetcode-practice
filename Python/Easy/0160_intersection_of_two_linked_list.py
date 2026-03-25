# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        path_A = headA
        path_B = headB

        while path_A!=path_B:
            path_B = path_B.next if path_B else headA
            path_A = path_A.next if path_A else headB
        return path_A