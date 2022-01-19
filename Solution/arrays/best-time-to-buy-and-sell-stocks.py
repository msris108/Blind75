from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # one transaction
        l, r = 0, 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
            else:
                # this else indicates that the right is the new low
                l = r
            r += 1
        
        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        # multiple transactions
        profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit += prices[i] - prices[i-1]
                
        return profit
        
        