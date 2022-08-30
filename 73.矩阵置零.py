#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

from typing import List
from copy import deepcopy

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        r, c = len(matrix), len(matrix[0])
        mat = deepcopy(matrix)

        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    for m in range(r):
                        matrix[m][j] = 0
                    for n in range(c):
                        matrix[i][n] = 0
        return matrix



# @lc code=end

matrix = [[1,1,1],[1,0,1],[1,1,1]]
s = Solution()
print(s.setZeroes(matrix=matrix))