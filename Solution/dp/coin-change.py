from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        
        dp[0] = 0 #  we can make $0 with 0 coins
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        print(dp[amount])
        
        return dp[-1] if dp[-1] != float('inf') else -1