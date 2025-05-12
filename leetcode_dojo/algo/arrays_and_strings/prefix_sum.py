from typing import List


def build_prefix_sum(arr):
    prefix = [arr[0]]
    for i in range(1, len(arr)):
        prefix.append(prefix[-1] + arr[i])
    
    return prefix

# If we want the sum of the subarray from i to j (inclusive), 
# then the answer is prefix[j] - prefix[i - 1], 
# or alternatively prefix[j] - prefix[i] + nums[i] if you don't want to deal with the out of bounds case when i = 0.

# prefix[j] - prefix[i] + nums[i]

# We MUST initialize our hash map with 0: 1, considering the empty prefix
# SUM of zero (empty array) appears once

from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            curr += num
            ans += counts[curr - k]
            counts[curr] += 1

        return ans