#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
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

    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 寻找没有左右子节点的数据
        if not root: return 0
        height = self.getDepth(root)
        return height

    def getDepth(self, root):
        if not root: return 0
        left_depth = self.getDepth(root.left)
        right_depth = self.getDepth(root.right)
        if not root.left and root.right:
            return 1 + right_depth
        if root.left and not root.right:
            return 1 + left_depth
        return 1 + min(left_depth, right_depth)
        

# @lc code=end

