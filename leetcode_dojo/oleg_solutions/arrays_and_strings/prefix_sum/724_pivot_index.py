# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/


from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        left_sum = 0
        right_sum = 0
        i = 0
        while True:
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum == right_sum:
                return i
            i += 1
            if i == len(nums):
                break
            left_sum = prefix_sum[i - 1]
        return -1


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1


solution = Solution2()
nums = [1, 7, 3, 6, 5, 6]
solution.pivotIndex(nums)
