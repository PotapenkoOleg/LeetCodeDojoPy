# 100. Same Tree
# https://leetcode.com/problems/same-tree/description/


# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p == None and q == None:
                return True
            
            if p == None or q == None:
                return False
            
            if p.val != q.val:
                return False
            
            return dfs(p.left, q.left) and dfs(p.right, q.right)
        return dfs(p,q)
        
class Solution2:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            stack = [(p,q)]
            while(stack):
                p, q = stack.pop()
                
                if p == None and q == None:
                    continue
                
                if p == None or q == None:
                    return False
                
                if p.val != q.val:
                    return False
                
                stack.append((p.right, q.right))
                stack.append((p.left, q.left))
            return True
                    
        return dfs(p,q)