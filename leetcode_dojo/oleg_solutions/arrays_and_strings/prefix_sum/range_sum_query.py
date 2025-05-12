# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/

from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.__nums = nums
        self.__prefix_sum = []
        self.__prefix_sum.append(nums[0])
        for i in range(1, len(nums)):
            self.__prefix_sum.append(self.__prefix_sum[-1] + nums[i])
        

    def sumRange(self, left: int, right: int) -> int:
        return self.__prefix_sum[right] - self.__prefix_sum[left] + self.__nums[left]