#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#
from dataclasses import dataclass
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and root.val == targetSum:
            return True
        left_result = self.hasPathSum(root.left, targetSum-root.val)
        right_result = self.hasPathSum(root.right, targetSum-root.val)
        return  left_result or right_result

# @lc code=end


