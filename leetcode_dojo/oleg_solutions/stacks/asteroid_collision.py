# Asteroid Collision
# https://leetcode.com/problems/asteroid-collision/description/

from typing import List

# [1,5,-5,6-6,5,3,7,-4]

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids)<2:
            return asteroids
        def process_asteroid(previous, current, stack):
            if abs(current) > abs(previous):
                stack.append(current)
            if abs(current) < abs(previous):
                stack.append(previous)

        stack = []
        
        for a in asteroids:
            stack.append(a)
            
            while True:
                current = stack.pop()
                previous = stack
            
            