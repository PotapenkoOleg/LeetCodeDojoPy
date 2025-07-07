# 1615. Maximal Network Rank
# https://leetcode.com/problems/maximal-network-rank/description/

from collections import defaultdict
from typing import List


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        neighbors = defaultdict(set)
        for road in roads:
            neighbors[road[0]].add(road[1])
            neighbors[road[1]].add(road[0])
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(neighbors[i]) + len(neighbors[j])
                if j in neighbors[i]:
                    rank -= 1
                ans = max(ans, rank)
        return ans