#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
#

from typing import Optional
# @lc code=start
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""

        s = str(root.val)

        if not root.left and not root.right:
            return s
        
        s += '({})'.format(self.tree2str(root.left))
        
        if root.right:
            s += '({})'.format(self.tree2str(root.right))
        return s

# @lc code=end

