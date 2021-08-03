from typing import List


class Solution:

    def num_islands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        island_count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == 1:
                    self.mark_island(grid, i, j)
                    island_count += 1
        return island_count

    def mark_island(self, grid, i, j):
        if i < 0 or i >= len(grid) or j <0 or j >= len(grid[i]) or grid[i][j] != 1:
            return
        grid[i][j] = 2
        self.mark_island(grid, i-1, j)
        self.mark_island(grid, i+1, j)
        self.mark_island(grid, i, j-1)
        self.mark_island(grid, i, j+1)
