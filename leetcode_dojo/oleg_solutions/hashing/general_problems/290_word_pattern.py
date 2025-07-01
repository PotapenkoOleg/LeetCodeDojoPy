# 290. Word Pattern
# https://leetcode.com/problems/word-pattern/description/

from collections import defaultdict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        if len(pattern) != len(words):
            return False
        hash1 = defaultdict(str)
        hash2 = defaultdict(str)
        p1 = 0
        p2 = 0
        while p1<len(pattern) and p2<len(words):
            p_cur = pattern[p1]
            w_cur = words[p2]
            hash_p = hash1.get(p_cur)
            hash_w = hash2.get(w_cur)
            if hash_p == None:
                if hash_w == None:
                    hash1[p_cur] = w_cur
                    hash2[w_cur] = p_cur
                    p1+=1
                    p2+=1
                    continue
                else:
                    return False
            if hash_p != w_cur or hash_w != p_cur:
                return False
            p1+=1
            p2+=1
        return True

            