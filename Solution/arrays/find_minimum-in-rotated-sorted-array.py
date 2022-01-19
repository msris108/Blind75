from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        minimum = nums[0]
        
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                # num is already sorted
                # minimum could have been previous mid. 
                minimum = min(minimum, nums[l])
                break
                
            m = l + (r - l) // 2
            minimum = min(minimum, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
                
        return minimum            
        