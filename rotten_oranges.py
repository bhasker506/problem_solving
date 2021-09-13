# You are given an m x n grid where each cell can have one of three values:

#     0 representing an empty cell,
#     1 representing a fresh orange, or
#     2 representing a rotten orange.

# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.


from collections import deque
from typing import List

class RottenOrangeIndex:
    
    def __init__(self, time_frame=0, index=(0,0)) -> None:
        self.time_frame = time_frame
        self.index = index
        

class RottenOranges:
    
    def rotten_oranges(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        max_timeframe = 0
        q = deque()
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 2:
                    q.append(RottenOrangeIndex(index=[i, j]))
        
        while len(q)!=0:
            rotten_orange = q.pop()
            directions = [(0,-1), (0,1), (-1,0),(1,0)]
            for direction in directions:
                x, y = rotten_orange.index
                x1, y1 = direction
                x += x1
                y += y1
                if x >=0 and x<len(grid) and y>=0 and y <len(grid[0]) and grid[x][y]==1:
                    time_frame = rotten_orange.time_frame
                    max_timeframe = time_frame+1
                    grid[x][y]=2
                    q.append(RottenOrangeIndex(time_frame=max_timeframe,index=[x, y]))
        print(grid)
        print(max_timeframe)
        return max_timeframe
            
if __name__ == '__main__':
    obj = RottenOranges()
    obj.rotten_oranges([[2,1,1],[1,1,0],[0,1,1]])             
