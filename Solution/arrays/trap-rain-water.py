from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        lmax = heights[l]
        rmax = heights[r]
        
        water = 0
        while l < r:
            if heights[l] < heights[r]:
                l += 1
                lmax = max(lmax, heights[l])
                water += lmax - heights[l]
            else:
                r -= 1
                rmax = max(rmax, heights[r])
                water += rmax - heights[r]
                
        return water