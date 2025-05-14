# 3005. Count Elements With Maximum Frequency
# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

from collections import Counter, defaultdict
from math import inf
from typing import List


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_freq = -inf
        frequencies = defaultdict(list)
        for k, v in counter.items():
            max_freq = max(max_freq, v)
            frequencies[v].append(k)
        return len(frequencies[max_freq])*max_freq
    
    
            
solution = Solution()
nums = [1,2,2,3,1,4]
solution.maxFrequencyElements(nums)