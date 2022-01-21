from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        
        for num in nums:
            # check if the number is the beginning of a sequence
            if num - 1 not in s:
                length = 0
                while num in s:
                    num += 1
                    length += 1
                longest = max(length, longest)
                
        return longest
                
            