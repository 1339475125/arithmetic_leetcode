#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
#
from utils.tree import generate_tree
from typing import Optional

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.getLeaf(root, 0)
        
    def getLeaf(self, root: Optional[TreeNode], sum):
        if not root:
            return 0
        sum = sum*2 + root.val
       
        if not root.left and not root.right:
            return sum
        return self.getLeaf(root.left, sum) + self.getLeaf(root.right, sum);


# @lc code=end


vals = [1,0,1,0,1,0,1]
tree = generate_tree(vals) 
sol = Solution()
print(sol.sumRootToLeaf(tree))
