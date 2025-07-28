# 79. Word Search
# https://leetcode.com/problems/word-search/description/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        def backtrack(row, col, i, seen):
            if len(word) == i:
                return True
            for dx, dy in directions:
                n_row, n_col = row + dx, col + dy
                if valid(n_row, n_col) and (n_row, n_col) not in seen:
                    if board[n_row][n_col] == word[i]:
                        seen.add((n_row, n_col))
                        if backtrack(n_row, n_col, i+1, seen):
                            return True
                        seen.remove((n_col, n_row))
            return False
        
        directions = [(0,1),(1,0),(0,-1),(-1, 0)]
        m = len(board)
        n = len(board[0])
        
        for row in range(m):
            for col in range(n):
                if board[m][n] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False
        
        