from typing import List

class Solution:
    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        
        # get the adjancency list
        # 0 to n - 1
        adjacency_list = { i: [] for i in range(num_courses) }
        
        for i in prerequisites:
            adjacency_list[i[0]].append(i[1])
            
        visited = set()
        def dfs(node):
            if node in visited:
                return False
            if adjacency_list[node] == []:
                return True
            
            visited.add(node)
            for i in adjacency_list[node]:
                if not dfs(i): return False
            visited.remove(node)
            adjacency_list[node] = [] # set to base condition
            
            return True
        
        for course in adjacency_list:
            if not dfs(course): return False
        
        return True