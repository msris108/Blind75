# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        p - previous
        c - current
        n - next
        
        n   1 > 2 > 3 > n
        n < 1   2 > 3 > n
        n < 1 < 2   3 > n
        n < 1 < 2 < 3   n
        '''
        
        p, c = None, head
        
        while c is not None:
            n = c.next
            
            # change links
            c.next = p
            
            # move forward
            p = c
            c = n
            
        return p
            
        