# 1496. Path Crossing
# https://leetcode.com/problems/path-crossing/description/

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        directions = {
            'N':(0,1),
            'E':(1,0),
            'S':(0,-1),
            'W':(-1,0)
        }
        visited = set()
        visited.add((0,0))
        prev_point = [0,0]
        for p in path:
            dir = directions[p]
            prev_point[0]+=dir[0]
            prev_point[1]+=dir[1]
            new_point = prev_point[0], prev_point[1]
            if new_point in visited:
                return True
            visited.add(new_point)
        return False
            
            