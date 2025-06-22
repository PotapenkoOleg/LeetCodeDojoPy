# 1436. Destination City
# https://leetcode.com/problems/destination-city/description/

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_set = set()
        dest_set = set()
        for src, dest in paths:
            src_set.add(src)
            dest_set.add(dest)
        for dest in dest_set:
            if dest not in src_set:
                return dest

class Solution2:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = zip(*paths)
        src_set = set(src)
        dest_set = set(dest)
        for dest in dest_set:
            if dest not in src_set:
                return dest

class Solution3:
    def destCity(self, paths: List[List[str]]) -> str:
        src, dest = zip(*paths)
        src_set = set(src)
        dest_set = set(dest)
        return dest_set.difference(src_set).pop()
        
solution = Solution3()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
solution.destCity(paths=paths)