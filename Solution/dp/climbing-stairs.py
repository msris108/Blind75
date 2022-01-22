from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)
        def rec(n):
            if n <= 1:
                return 1
            return rec(n-1) + rec(n-2)
        return rec(n)

class Solution:
    @lru_cache(None)
    def climbStairs(self, n: int) -> int:
        if n <= 1: return 1 
        return self.climbStairs(n-1) + self.climbStairs(n-2)