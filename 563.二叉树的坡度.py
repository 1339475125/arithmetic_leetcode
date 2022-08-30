#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
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
        self.res = 0

    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.get_sum(root)
        return self.res

    def get_sum(self, root: Optional[TreeNode]):
        if not root:
            return 0
        left_node = self.get_sum(root.left)
        right_node = self.get_sum(root.right)
        self.res = abs(left_node  - right_node)
        return left_node + right_node + root.val

# @lc code=end

