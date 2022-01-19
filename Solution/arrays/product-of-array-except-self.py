from typing import List

class Solution:
    '''
    logic -> used a prefix and postfix array
    '''
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # space O(n) -> bad 
    #     prefix = nums.copy()
    #     postfix = nums.copy()
        
    #     for i in range(1, len(nums)):
    #         prefix[i] *= prefix[i-1]
            
    #     for i in reversed(range(0, len(nums) - 1)):
    #         postfix[i] *= postfix[i+1]
            
    #     res = [postfix[1]] # postfix of 1st element has it has no prefix
    #     for i in range(1, len(nums) - 1):
    #         res.append(prefix[i-1] * postfix[i+1])
    #     res.append(prefix[-2]) # postfix of 1st element has it has no postfix

    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # O(1) space - better

        res = [1] * len(nums)
        
        prefix = 1        
        for i in range(len(nums)):
            res[i] *= prefix # res[i] = prefix 
            prefix *= nums[i]
            
        postfix = 1         
        for i in reversed(range(len(nums))):
            res[i] *= postfix
            postfix *= nums[i]
            
        return res