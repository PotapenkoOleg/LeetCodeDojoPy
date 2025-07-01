# 735. Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

from collections import deque
from typing import List

# [1,5,-5,6,-6,5,3,7,-4]
# !!! [-2,-1,1,2]

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)<2:
            return asteroids
        p_ = 0
        stack = []
        while p_ < len(asteroids):
            current = asteroids[p_]
            stack.append(current)
            while stack and len(stack)>1:
                if stack[-2] > 0 and stack[-1] < 0:
                    current = stack.pop()
                    if abs(stack[-1]) < abs(current):
                        stack.pop()
                        stack.append(current)
                        continue
                    if abs(stack[-1]) == abs(current):
                        stack.pop()
                        break
                    if abs(stack[-1]) > abs(current):
                        break
                else:
                    break
            p_ += 1
        return stack
    
    
solution = Solution()
x = solution.asteroidCollision([-2,-1,1,2])
print(x)
                        
                    

                
                
            

            

            
            