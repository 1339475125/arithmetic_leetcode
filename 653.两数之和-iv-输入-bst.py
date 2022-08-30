#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入 BST
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
        self.res = {}
        self.flag = False

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return self.flag
        self.get_target(root, k)
        return self.flag
        
    def get_target(self, root, k):
        if not root:
            return
        if root:
            temp = k - root.val
            if self.res.get(root.val, None):
                self.flag = True
                return 
            self.res[temp] = 1
        self.get_target(root.left, k)
        self.get_target(root.right, k)

# @lc code=end

