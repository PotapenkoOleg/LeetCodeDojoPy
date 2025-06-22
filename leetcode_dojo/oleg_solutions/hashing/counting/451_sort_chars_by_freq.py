# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/

from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        frequencies = defaultdict(list)
        for k,v in counter.items():
            frequencies[v].append(k)
        ans = []
        for k in sorted(frequencies.keys(), reverse=True):
            for v in frequencies[k]:
                ans.append(v*k)
        return "".join(ans)

solution = Solution()
s = "tree"
solution.frequencySort(s)