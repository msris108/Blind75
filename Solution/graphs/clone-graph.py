# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
            hashmap that stores the old nodes -> new nodes(copy)
            if the old node already visited return the mapping, else
            create a new node with the same value and map the neighbors
        '''
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy
            
            for i in node.neighbors:
                copy.neighbors.append(dfs(i))        
            return copy
    
        copy_node = dfs(node)
        print(old_to_new)
        return copy_node
            
        
        