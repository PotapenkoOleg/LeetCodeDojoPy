# 872. Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/description/

# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves):
            if not root:
                return
            
            if root.left == None and root.right == None:
                leaves.append(root.val)
                return
            
            dfs(root.left, leaves)
            dfs(root.right, leaves)
        
        leaves1 = []
        dfs(root1, leaves1)
        
        leaves2 = []
        dfs(root2, leaves2)
        
        if len(leaves1) != len(leaves2):
            return False

        while leaves1:
            val1 = leaves1.pop()
            val2 = leaves2.pop()
            if val1 != val2:
                return False
        return True

class Solution2:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root, leaves):
            if not root:
                return
            stack = [root]
            while stack:
                root = stack.pop()
                if root.left == None and root.right == None:
                    leaves.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)
        
        leaves1 = []
        dfs(root1, leaves1)
        
        leaves2 = []
        dfs(root2, leaves2)
        
        if len(leaves1) != len(leaves2):
            return False

        while leaves1:
            val1 = leaves1.pop()
            val2 = leaves2.pop()
            if val1 != val2:
                return False
        return True
        
                