# 1732. Find the Highest Altitude
# https://leetcode.com/problems/find-the-highest-altitude/description/


# Example 1:
# Input: gain = [-5,1,5,0,-7]
# Output: 1
# Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.

# Example 2:
# Input: gain = [-4,-3,-2,-1,4,3,2]
# Output: 0
# Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.


from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        prefix_sum = 0
        for cur in gain:
            prefix_sum = prefix_sum + cur
            ans = max(ans, prefix_sum)
        return ans
            
        
        