#
# @lc app=leetcode.cn id=501 lang=python3
#
# [501] 二叉搜索树中的众数
#
from typing import Dict, Optional, List
# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res = {}
        self.getMode(root, res)
        # print(res)
        max_data = max(res.items(), key=lambda x:x[1])[1]
        return [k for k, v in res.items() if v == max_data]

    def getMode(self, root: Optional[TreeNode], res = {}) ->None:
        if not root:
            return
        res[root.val] = res.get(root.val, 0) + 1
        # print(res)
        self.getMode(root.left, res=res)
        self.getMode(root.right, res=res)
        return
    
        
# @lc code=end
# node = TreeNode()
# solution = Solution()
# print(solution.findMode(node))

