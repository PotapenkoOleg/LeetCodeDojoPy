# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        prefix_sum = 0
        for cur in gain:
            prefix_sum = prefix_sum + cur
            ans = max(ans, prefix_sum)
        return ans
