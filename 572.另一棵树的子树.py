#
# @lc app=leetcode.cn id=572 lang=python3
#
# [572] 另一棵树的子树
#

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if self.subTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def subTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        if root.val != subRoot.val:
            return False
        return self.subTree(root.left, subRoot.left) and self.subTree(root.right, subRoot.right) 
        

# @lc code=end
# node5 = TreeNode(2)
# node4 = TreeNode(1)
# node1 = TreeNode(4, left=node4)
# node2 = TreeNode(5, left=node5)
# node0 = TreeNode(3, left=node1, right=node2)

# node01 = TreeNode(1)
# node02 = TreeNode(2)
# node00 = TreeNode(3, left=node01, right=node02)

# solution = Solution()
# print(solution.isSubtree(node0, node00))