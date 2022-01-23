from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                # if the new interval is before (non overlapping) current interval 
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # if the new interval is completely infront of the current interval
                res.append(intervals[i])
            else:
                # do not append as the modified interval could still overlap
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # if the new interval is greater than all the intervals 
        res.append(newInterval)
        return res
                