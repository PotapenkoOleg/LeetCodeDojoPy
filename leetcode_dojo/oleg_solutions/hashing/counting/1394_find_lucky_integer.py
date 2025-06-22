# 1394. Find Lucky Integer in an Array
# https://leetcode.com/problems/find-lucky-integer-in-an-array/description/

from collections import Counter
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)
        ans = -1
        for k,v in counter.items():
            if k==v:
                ans = max(ans, k)
        return ans