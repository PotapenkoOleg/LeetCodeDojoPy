# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def index_to_row_col(index):
            row = index // n
            col = index % n
            return (row, col)
        
        left = 0
        right = m*n-1
        while(left<=right):
            mid = (left+right) // 2
            row, col = index_to_row_col(mid)
            element = matrix[row][col]
            if element == target:
                return True
            if element < target:
                left = mid + 1
                continue
            if element > target:
                right = mid - 1
                continue
        return False
                
            