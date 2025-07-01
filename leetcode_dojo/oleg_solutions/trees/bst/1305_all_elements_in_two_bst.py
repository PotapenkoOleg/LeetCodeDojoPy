# 1305. All Elements in Two Binary Search Trees
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/

# Definition for a binary tree node.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        def inorder_dfs(root, accum):
            if not root:
                return
            inorder_dfs(root.left, accum)
            accum.append(root.val)
            inorder_dfs(root.right, accum)
        accum1=[]
        inorder_dfs(root1, accum1)
        accum2=[]
        inorder_dfs(root2,accum2)
        ans = []
        p1=0
        p2=0
        while p1 < len(accum1) and p2 < len(accum2):
            if accum1[p1] < accum2[p2]:
                ans.append(accum1[p1])
                p1+=1
            else:
                ans.append(accum2[p2])
                p2+=1
        while p1 < len(accum1):
            ans.append(accum1[p1])
            p1+=1
        while p2 < len(accum2):
            ans.append(accum2[p2])
            p2+=1
        return ans
        
            
        
                
        