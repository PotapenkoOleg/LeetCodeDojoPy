# 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/description/

# Example 1:
# Input: nums = 
# [ 1, 7,  3,  6,  5,  6]
# [ 1, 8, 11, 17, 22, 28]
# Output: 3
# Explanation:
# The pivot index is 3.
# Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
# Right sum = nums[4] + nums[5] = 5 + 6 = 11

# Example 2:
# Input: nums = [1,2,3]
# Output: -1
# Explanation:
# There is no index that satisfies the conditions in the problem statement.

# Example 3:
# Input: nums = [2,1,-1]
# Output: 0
# Explanation:
# The pivot index is 0.
# Left sum = 0 (no elements to the left of index 0)
# Right sum = nums[1] + nums[2] = 1 + -1 = 0

from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        prefix_sum = []
        prefix_sum.append(nums[0])
        for i in range(1,len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        left_sum = 0
        right_sum = 0
        i = 0
        while True:
            right_sum = prefix_sum[-1] - prefix_sum[i]
            if left_sum == right_sum:
                return i
            i+=1
            if i == len(nums):
                break
            left_sum = prefix_sum[i-1] 
        return -1

class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum = 0
        right_sum = 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i] 
        return -1
        
    
solution = Solution2()
nums = [ 1, 7,  3,  6,  5,  6]
solution.pivotIndex(nums)