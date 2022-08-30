#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

from turtle import right
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

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.mfs(root, root)
    
    def mfs(self, left_root, right_root):
        if not left_root and not right_root:
            return True
        if not left_root or not right_root:
            return False
        return self.mfs(left_root.left, right_root.right) and left_root.val==right_root.val  and self.mfs(left_root.right, right_root.left)


# @lc code=end
# node = TreeNode(
#     val = 1,
#     left = TreeNode(val=2, right=TreeNode(val=3)),
#     right = TreeNode(val=2, right=TreeNode(val=3))
# )
# node = TreeNode(
#     val = 1,
#     left = TreeNode(val=2, left=TreeNode(val=3), right=TreeNode(val=4)),
#     right = TreeNode(val=2, left=TreeNode(val=4), right=TreeNode(val=3))
# )
# solution = Solution()
# print(solution.isSymmetric(node))