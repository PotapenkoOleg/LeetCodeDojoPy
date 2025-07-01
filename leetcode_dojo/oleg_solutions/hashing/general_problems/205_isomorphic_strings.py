# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/description/

from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash1 = defaultdict(str)
        hash2 = defaultdict(str)
        p1 = 0
        p2 = 0
        while p1 < len(s):
            s_cur = s[p1]
            t_cur = t[p2]
            hash_s = hash1.get(s_cur)
            hash_t = hash2.get(t_cur)
            if hash_s == None:
                if hash_t == None:
                    hash1[s_cur] = t_cur
                    hash2[t_cur] = s_cur
                    p1 += 1
                    p2 += 1
                    continue
                else:
                    return False
            if hash_s != t_cur:
                return False
            p1 += 1
            p2 += 1
        return True

solution = Solution()
s = "badc"
t = "baba"
solution.isIsomorphic(s, t)
    