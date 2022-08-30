#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            return False
        node1, node2 = [], []
        self.getLeaf(root1, res=node1)
        self.getLeaf(root2, res=node2)
        print(node1, node2)
        return True if node1==node2 else False

    def getLeaf(self, root: Optional[TreeNode], res= []):
        if not root:
            return
        self.getLeaf(root.left, res)
        if not root.left and not root.right:
            res.append(root.val)
        self.getLeaf(root.right, res)
        return

# @lc code=end

