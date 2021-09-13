# 56. Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

from typing import List


class MergerIntervals:
    
    def merge_intervals(self, intervals: List) -> List:
        
        if len(intervals) <= 1:
            return intervals
        
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        current_interval = sorted_intervals[0]
        result = [current_interval]
        
        for interval in sorted_intervals[1:]:
            current_end = current_interval[1]
            next_start = interval[0]
            next_end = interval[1]
            if current_end >= next_start:
                current_interval[1] = max(current_end, next_end)
            else:
                current_interval = interval
                result.append(current_interval)
        
        return result


if __name__ == '__main__':
    obj = MergerIntervals()
    print(obj.merge_intervals([[1,3],[2,6],[8,10],[15,18]]))
        