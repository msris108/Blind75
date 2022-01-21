from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        edges = []
        for i in range(N):
            for j in range(N):
                if isConnected[i][j] == 1:
                    edges.append([i, j])
                    
                    
        par = [ i for i in range(N) ]
        rank = [1] * N
        
        def find(n1):
            res = n1
            
            while res != par[res]:
                par[res] = par[par[res]] # optimization -> works on commenting
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            
            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1] 
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return 1
    
        res = N
        for n1, n2 in edges:
            res -= union(n1, n2)
            
        return res

                
        
                    
            
        