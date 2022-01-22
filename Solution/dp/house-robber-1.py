from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # space o(n)
        # dp = [0] * len(nums)
        
        # if len(nums) == 1: return nums[0]
        
        # dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        # for i in range(2, len(nums)):
        #     dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        # return dp[len(nums) - 1]
        
        #space o(1)
        
        rob1, rob2 = 0, 0
        
        for num in nums:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        # tuple assignment is slower :(
        # rob1, rob2 = 0, 0
        
        # for num in nums:
        #     rob1, rob2 = rob2, max(num + rob1, rob2)
        
        # return rob2
        
