# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        merged = temp
        
        while list1 or list2:
            val1 = list1.val if list1 else float('inf')
            val2 = list2.val if list2 else float('inf')

            if val1 < val2:
                merged.next = ListNode(val1)
                merged = merged.next
                list1 = list1.next if list1 else None
            else:
                merged.next = ListNode(val2)
                merged = merged.next
                list2 = list2.next if list2 else None

        return temp.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        merged = temp
        
        while list1 and list2:
            val1 = list1.val
            val2 = list2.val

            if val1 < val2:
                merged.next = ListNode(val1)
                merged = merged.next
                list1 = list1.next 
            else:
                merged.next = ListNode(val2)
                merged = merged.next
                list2 = list2.next 

        if list1:
            merged.next = list1
        else:
            merged.next = list2

        return temp.next