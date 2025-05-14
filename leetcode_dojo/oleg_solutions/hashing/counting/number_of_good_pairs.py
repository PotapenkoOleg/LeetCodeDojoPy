# 1512. Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/description/

from collections import defaultdict
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = defaultdict(list)
        for i, num in enumerate(nums):
            counts[num].append(i)
        ans = 0 
        for v in counts.values():
            if len(v) < 2:
                continue
            ans+=sum(range(len(v)))
        return ans