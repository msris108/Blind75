from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
            
        for i in range(len(nums) + 1):
            print(i)
            res ^= i
        
        return res

        # slower, but same complexity
        # n = len(nums) + 1
        # return (n * (n - 1)) // 2 - sum(nums)