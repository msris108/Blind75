from typing import List

'''
    given words in a dictionary lexicographical order
    return possible char seq order
    if not possible return ""

    1. asdf
    2. asd

    is incorrect case as lexicographiocally this makes no sense so return ""

    algo: topological sort
    
    1. asdx 
    2. asdf 

    find first differeing word : x, f
    x comes before f in the new language

    make a node x -> f

    make for all possible nodes
    check for cycle if cycle(True) return "" (rule association is not possible) -> using post order dfs
    else append to res

'''

class Solution:
    def alienDictionary(self, words: List) -> str:
        adj = { c: set() for w in words for c in w }

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return "" # trivial edge case where 1. asder 2. asd <- incorrent

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = {} # False -> visited and True -> visited and explored
        res = []

        def dfs(c):
            if c in visited:
                return visited[c] # loop found

            visited[c] = True
            for nei in adj[c]:
                if dfs(nei):
                    return True
            visited[c] = False

            # post order dfs
            res.append(c)

        for c in adj:
            if dfs(c):
                return "" # cycle detected

        res.reverse()
        return "".join(res)         

            



