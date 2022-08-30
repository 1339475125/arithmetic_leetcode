#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = 0
        if not root:
            return 0
            
        if root.left and root.left.left == None and root.left.right == None:
            result += root.left.val

        result += self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        return result

# @lc code=end

