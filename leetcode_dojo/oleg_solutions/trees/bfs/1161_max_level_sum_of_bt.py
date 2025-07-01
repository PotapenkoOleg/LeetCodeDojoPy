# 1161. Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/


# Definition for a binary tree node.

from collections import defaultdict, deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        sums = defaultdict(list)
        cur_level = 0
        queue = deque([root])
        while queue:
            cur_level += 1
            num_nodes_cur_level = len(queue)
            cur_level_sum = 0 
            for _ in range(num_nodes_cur_level):
                cur_node = queue.popleft()
                cur_level_sum += cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            sums[cur_level_sum].append(cur_level)
        max_sum = max(sums.keys())
        min_level = min(sums[max_sum])
        return min_level
    
class Solution2:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_sum = float('-inf')
        min_level = 0
        cur_level = 0
        queue = deque([root])
        while queue:
            cur_level += 1
            num_nodes_cur_level = len(queue)
            cur_level_sum = 0 
            for _ in range(num_nodes_cur_level):
                cur_node = queue.popleft()
                cur_level_sum += cur_node.val
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            if cur_level_sum > max_sum:
                max_sum = cur_level_sum
                min_level = cur_level
        return min_level