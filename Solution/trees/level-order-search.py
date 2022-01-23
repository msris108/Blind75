# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        queue = deque( [root] )
        
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    tmp.append(node.val)    
                    queue.append(node.left) 
                    queue.append(node.right)
            if tmp:
                res.append(tmp)
            
        return res