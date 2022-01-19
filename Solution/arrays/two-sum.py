from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # time: O(n) | space: O(n)
        d = {}
        for i, num in enumerate(nums):
            match = target - num
            if match in d:
                return [d[match], i]
            else:
                d[num] = i

'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # return numbers O(nlogn) O(n)
        nums.sort()
        l = 0
        r = len(nums) - 1
        while l < r:
            curr_sum = nums[l] + num[r]
            if curr_sum < target:
                l += 1
            elif curr_sum > target:
                r -= 1
            else:
                return [l, r]
        
        return [-1, -1]
'''

