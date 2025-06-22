# 2958. Length of Longest Subarray With at Most K Frequency
# https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/

from collections import Counter
from typing import List


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = Counter()
        left = -1
        ans = 0
        for right in range(len(nums)):
            freq[nums[right]]+=1
            while freq[nums[right]] > k:
                left+=1
                freq[nums[left]]-=1
            ans = max(ans, right-left)
        return ans