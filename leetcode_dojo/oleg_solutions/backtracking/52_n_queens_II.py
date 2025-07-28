# 52. N-Queens II
# https://leetcode.com/problems/n-queens-ii/description/


class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(c_row, cols, diags, anti_diags):
            if c_row == n:
                return 1
            
            solutions = 0
            for c_col in range(n):
                c_diag = c_row - c_col
                c_anti_diag = c_row + c_col
                
                if (c_col in cols) or (c_diag in diags) or (c_anti_diag in anti_diags):
                    continue
                cols.add(c_col)
                diags.add(c_diag)
                anti_diags.add(c_anti_diag)
                solutions += backtrack(c_row+1, cols, diags, anti_diags)
                cols.remove(c_col)
                diags.remove(c_diag)
                anti_diags.remove(c_anti_diag)
            return solutions
                
        
        return backtrack(0, set(), set(), set())
        