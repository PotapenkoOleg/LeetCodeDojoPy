# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/description/

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        in_out_degrees = [0] * (n + 1)
        for a, b in trust:
            in_out_degrees[a] -= 1
            in_out_degrees[b] += 1
        for i,in_out_degree in enumerate(in_out_degrees[1:], start=1):
            if in_out_degree == n-1:
                return i
        return -1