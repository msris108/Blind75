from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i, num in enumerate(nums):
            # same number do not repeat
            if i > 0 and  num == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                cur_sum = num + nums[l] + nums[r]
                
                if cur_sum == 0:
                    res.append([num, nums[l], nums[r]])
                    # we have to move left pointer until new number comes 
                    l += 1
                    while nums[l] == nums[l -1] and l < r:
                        l += 1
                elif cur_sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        return res
            

sol = Solution()
print(sol.threeSum(nums = [-1,0,1,2,-1,-4]))