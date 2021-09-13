# 253. Meeting Rooms II
# Medium

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

 

# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

 

# Constraints:

#     1 <= intervals.length <= 104
#     0 <= starti < endi <= 106


from typing import List
import heapq

class MeetingRooms2:
    
    def meeting_rooms(self, intervals: List) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        free_rooms = []
        heapq.heappush(free_rooms, intervals[0][1])
        for i in intervals[1:]:
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        return len(free_rooms)
    
if __name__ == '__main__':
    m = MeetingRooms2()
    print(m.meeting_rooms([[0,30],[5,10],[15,20]]))
        