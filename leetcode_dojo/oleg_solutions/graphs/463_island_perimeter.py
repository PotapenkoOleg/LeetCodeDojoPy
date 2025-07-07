# 463. Island Perimeter
# https://leetcode.com/problems/island-perimeter/description/

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ans = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    ans += 4
                    if row > 0 and grid[row-1][col] == 1:
                        ans -= 2
                    if col > 0 and grid[row][col-1] == 1:
                        ans -= 2
        return ans