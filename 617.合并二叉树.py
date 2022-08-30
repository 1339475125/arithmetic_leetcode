#
# @lc app=leetcode.cn id=617 lang=python3
#
# [617] 合并二叉树
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
    def mergeTrees(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> Optional[TreeNode]:
        if t1 and t2:                                               # 如果输入的两个结点均不为空
            t1.val += t2.val                                        # 结点值相加
            t1.left = self.mergeTrees(t1.left, t2.left)             # 合并左子树
            t1.right = self.mergeTrees(t1.right, t2.right)          # 合并右子树
            return t1                                               # 返回t1
        return t1 or t2                                     
    
# @lc code=end

