#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
#

# /**
#  中序遍历: 
#  利用性质: 从小到大的  任意两节点的差只需要遍历相邻节点的差即可(而且不用绝对值 (大-小)肯定>0)
#  */
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
        self.pre = "null"
        self.min_data = 10**5 + 1

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.dfs(root)
        return self.min_data
    
    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return
        self.dfs(root.left)
        if self.pre != "null":
            self.min_data = min(self.min_data, root.val - self.pre.val)
        print(self.min_data)
        self.pre = root
        self.dfs(root.right)

        
# @lc code=end


