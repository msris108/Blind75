class Solution:
    '''
    ALGORITHM
    ---------
    1. check if the middle is associated with the left half of the array or right half of the array
    2. if left :
        2.1 if target is less than the left-most element (or) target is greater than middle: search right ( l = m + 1 )
            else search left ( r = m - 1)
       else :
        2.2 if target is greater than the right-most element (or) target is smaller than middle: search left
            else search right
    '''
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m  = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # left sorted portion
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
        return -1