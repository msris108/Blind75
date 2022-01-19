from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
            we maintain both max product and min product
            if the next the number is +ve then mult by max, else multiply by min
            
            edge case : 0
            any time you get zero max = min = 1
        '''
        res = max(nums)
        minimum, maximum = 1, 1
        
        for num in nums:
            if num == 0:
                minimum, maximum = 1, 1
                continue
                
            tmp = num * maximum
            maximum = max(num * minimum, num * maximum, num)
            minimum = min(num * minimum, tmp, num)
            
            # IMP: COMMON MISTAKE the maximum is already while computing the minimum, thus we need to store the previous maximum in tmp
            
            res = max(res, maximum)
                
        return res