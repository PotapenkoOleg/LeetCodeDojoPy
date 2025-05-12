# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

from math import inf
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = cur = 0
        ans = inf
        for right in range(len(nums)):
            cur += nums[right]
            while (cur >= target):
                lenght = right - left + 1
                ans = min(ans, lenght)
                cur -= nums[left]
                left += 1
        return 0 if ans == inf else ans
