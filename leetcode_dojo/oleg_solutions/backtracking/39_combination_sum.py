# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans  = []
        def backtrack(path, i, cur_sum):
            if cur_sum == target:
                ans.append(path[:])
                return
            
            for i in range(i, len(candidates)):
                cur = candidates[i]
                if cur + cur_sum <= target:
                    path.append(cur)
                    backtrack(path, i, cur+cur_sum)
                    path.pop()
        
        backtrack([], 0, 0)
        return ans
            
        