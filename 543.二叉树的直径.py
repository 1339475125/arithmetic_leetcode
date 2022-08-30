#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from itertools import count
from turtle import right
from typing import Optional
from unittest import result

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depth(root)
        return self.result
        
    def depth(self, root):
        if not root:
            return 0
        left_depth = self.depth(root.left)
        right_depth = self.depth(root.right)
        self.result = max(self.result, left_depth + right_depth)
        return max(left_depth, right_depth) +1
        

# @lc code=end

