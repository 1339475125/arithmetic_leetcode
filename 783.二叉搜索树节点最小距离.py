#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
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
        self.pre: TreeNode = None
        self.min_data = 10**5 +1

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.minDiff(root)
        return self.min_data
        
    def minDiff(self, root: TreeNode):
        if not root:
            return
        self.minDiff(root.left)
        if self.pre:
            self.min_data = min(self.min_data, root.val - self.pre.val)
        self.pre = root
        self.minDiff(root.right)
# @lc code=end

