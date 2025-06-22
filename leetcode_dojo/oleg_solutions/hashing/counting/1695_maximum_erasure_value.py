# 1695. Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/description/

from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = set()
        ans = 0 
        score = 0
        left = 0
        for right in range(len(nums)):
            while(nums[right] in s):
                score-=nums[left]
                s.remove(nums[left])
                left+=1
            s.add(nums[right])
            score+=nums[right]
            ans = max(ans, score)
        return ans