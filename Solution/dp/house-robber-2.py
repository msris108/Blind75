from typing import List

class Solution:
    '''
    logic since houses in a cycle 
    first and last connected
    ans = max -> { houseRobber1(arr - {first}), houseRobber1(arr - {last}) 
    '''
    def rob(self, nums: List[int]) -> int:
        def house_robber1(nums):
            rob1, rob2 = 0, 0
            for num in nums:
                rob1, rob2 = rob2, max(num + rob1, rob2)
            return rob2
            
        # the input array can only be one element so max(the only ele, arr - {first ele}, arr - {last ele})
        return max(nums[0], house_robber1(nums[1:]), house_robber1(nums[:-1]))