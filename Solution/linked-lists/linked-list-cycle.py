class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # using fast pointer - slow pointer approach
    
        if head is None or head.next is None or head.next.next is None: return False # zero / one / two Nodes
        
        slow = head.next
        fast = head.next.next
        
        while fast is not None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
            
        return False