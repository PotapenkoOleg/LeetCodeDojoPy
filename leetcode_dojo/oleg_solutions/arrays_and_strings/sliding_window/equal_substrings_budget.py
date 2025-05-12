# 1208. Get Equal Substrings Within Budget
# https://leetcode.com/problems/get-equal-substrings-within-budget/description/


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:

        length = len(s)
        ans = 0
        cur_len = 0
        cur_cost = 0
        left = 0
        costs = []

        for i in range(len(s)):
            costs.append(abs(ord(s[i]) - ord(t[i])))

        for right in range(length):
            cur_len += 1
            cur_cost += costs[right]
            while (cur_cost > maxCost):
                cur_len -= 1
                cur_cost -= costs[left]
                left += 1
            ans = max(ans, cur_len)
        return ans
