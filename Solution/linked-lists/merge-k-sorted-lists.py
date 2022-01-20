# Definition for singly-linked list.
from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
import heapq

class ListObject:
    def __init__(self, idx, val):
        self.idx = idx
        self.val = val
        
    def __lt__(self, other):
        return self.val < other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]

        # result 
        result = ListNode()
        merged = result
        
        vals = [ListObject(i, l.val if l else float('inf') ) for i, l in enumerate(lists)]
        heapq.heapify(vals)
        
        while any(lists):
            min_ele = heapq.heappop(vals)
            min_val_idx, min_val = min_ele.idx, min_ele.val
                        
            # create new node and shift merged
            merged.next = ListNode(min_val)
            merged = merged.next
            
            # move the node in lists
            lists[min_val_idx] = lists[min_val_idx].next
            
            # update value in vals
            val = lists[min_val_idx].val if lists[min_val_idx] else float('inf')
            heapq.heappush(vals, ListObject(min_val_idx, val))
        
#         vals = [l.val if l else float('inf') for l in lists]
#         while any(lists):
#             min_val = min(vals)
#             min_val_idx = vals.index(min_val)
            
#             # create new node and shift merged
#             merged.next = ListNode(min_val)
#             merged = merged.next
            
#             # move the node in lists
#             lists[min_val_idx] = lists[min_val_idx].next
            
#             # update value in vals
#             vals[min_val_idx] = lists[min_val_idx].val if lists[min_val_idx] else float('inf')
            
        return result.next