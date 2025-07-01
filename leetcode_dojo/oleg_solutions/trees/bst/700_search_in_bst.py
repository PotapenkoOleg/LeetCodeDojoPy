# 700. Search in a Binary Search Tree
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        next_node = root
        while next_node:
            if next_node.val == val:
                return next_node
            if next_node.val < val:
                next_node = next_node.right
                continue
            if next_node.val > val:
                next_node = next_node.left
                continue
        return next_node