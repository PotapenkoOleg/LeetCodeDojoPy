# 2540. Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/

from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                return nums1[p1]
            if nums1[p1] < nums2[p2]:
                p1 += 1
                continue
            if nums1[p1] > nums2[p2]:
                p2 += 1
                continue
        return -1


solution = Solution()
nums1 = [1, 2, 3, 6]
nums2 = [2, 3, 4, 5]
result = solution.getCommon(nums1, nums2)
pass
