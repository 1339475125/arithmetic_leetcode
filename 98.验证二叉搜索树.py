#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
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
        self.flag = True
        self.pre = None

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        self.is_valid_bst(root)
        return self.flag

    def is_valid_bst(self, root: Optional[TreeNode]):
        if not root:
            return
        self.is_valid_bst(root.left)
        if self.pre and self.pre.val >= root.val:
            self.flag = False
        self.pre = root
        self.is_valid_bst(root.right)
        return

        
# @lc code=end