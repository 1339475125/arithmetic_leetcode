#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

from typing import List
# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, n -1
        while l  < m and r >= 0:
            if matrix[l][r] == target:
                return True
            if matrix[l][r] < target:
                l += 1
            else:
                r -= 1
        return False

        
# @lc code=end

