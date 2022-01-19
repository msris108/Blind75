from typing import List

class Solution:
    def trap(self, heights: List[int]) -> int:
        # space O(n) -> bad, refer arrays for optimal solution
        # left max 
        left_max_array = []
        left_max = 0
        for height in heights:
            left_max = max(left_max, height)
            left_max_array.append(left_max)
            
        # right max 
        right_max_array = []
        right_max = 0
        for height in reversed(heights):
            right_max = max(right_max, height)
            right_max_array.append(right_max)
        right_max_array = right_max_array[::-1]
        
        print(right_max_array, left_max_array)
        water = 0
        for i, height in enumerate(heights):
            min_height = min(left_max_array[i], right_max_array[i])
        
            if height < min_height:
                water += min_height - height
                
        return water