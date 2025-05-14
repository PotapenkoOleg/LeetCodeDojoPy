# 1748. Sum of Unique Elements
# https://leetcode.com/problems/sum-of-unique-elements/description/

from collections import Counter
from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return sum([k for k in counter.keys() if counter[k]==1])

        

solution = Solution()
nums = [2,2,2,2]
solution.sumOfUnique(nums)