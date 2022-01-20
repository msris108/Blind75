# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def reverseList(head):
            p, c = None, head

            while c is not None:
                n = c.next
                c.next = p
                p = c
                c = n

            return p
        
        def lenList(head):
            node = head
            l = 0
            while node:
                node = node.next
                l += 1
            return l+1
        
        def deleteNode(head, n):
            node = head
            if n == 1:
                return node.next
            else:
                while n - 2 > 0:
                    node = node.next
                    n -= 1
                node.next = node.next.next if node.next else None
            return head
        
        return deleteNode(head, lenList(head) - n)

        # return reverseList(deleteNode(reverseList(head), n))
            
        