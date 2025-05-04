# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/

from typing import List


# [4,3,0,0,0,5,0,7, 9,99]


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ins_pos = 0
        cur_pos = 0
        while cur_pos < len(nums):
            nums[ins_pos] = nums[cur_pos]
            cur_pos += 1
            if nums[ins_pos] != 0:
                ins_pos += 1
        while ins_pos < len(nums):
            nums[ins_pos] = 0
            ins_pos += 1


solution = Solution()
nums = [0]  # [4,3,0,0,0,5,0,7, 9,99]
solution.moveZeroes(nums)
pass
