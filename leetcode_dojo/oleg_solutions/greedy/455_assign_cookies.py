# 455. Assign Cookies
# https://leetcode.com/problems/assign-cookies/description/

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        g_index=0
        s_index=0
        ans=0
        while g_index<len(g) and s_index<len(s):
            if s[s_index]>=g[g_index]:
                g_index+=1
                ans+=1
            s_index+=1
        return ans