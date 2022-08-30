#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        queue = [(root, 0)]
        max_wid = 1
        
        while queue:
            layer = []
            while queue:
                node = queue.pop(0)
                if node[0].left:
                    layer.append((node[0].left, node[1]*2))
                if node[0].right:
                    layer.append((node[0].right, node[1]*2+1))
            if layer:
                queue = layer
                max_wid = max(max_wid, layer[-1][1] - layer[0][1] + 1)
        
        return max_wid

# @lc code=end

