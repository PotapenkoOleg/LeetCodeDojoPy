# 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/description/

from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort(reverse=True)
        ans = 0
        while costs and coins > 0:
            cur_cost = costs.pop()
            if cur_cost > coins:
                break
            else:
                coins -= cur_cost
                ans += 1
        return ans