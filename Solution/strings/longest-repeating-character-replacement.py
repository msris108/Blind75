# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         hashmap = {}
#         res = 0
        
#         l = 0
#         for r in range(len(s)):
#             hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            
#             while (r - l + 1) - max(hashmap.values()) > k:
#                 hashmap[s[l]] -= 1
#                 l += 1
                
#             res = max(r - l + 1, res)
            
#         return res
            
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        res = 0
        
        l = 0
        maxf = 0 # improving the max() operation which is O(n) or O(26) to O(1) which keeps the max freq at any point of time (ref video)
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            maxf = max(maxf, hashmap[s[r]])
            while (r - l + 1) - maxf> k:
                hashmap[s[l]] -= 1
                l += 1
                
            res = max(r - l + 1, res)
            
        return res
        