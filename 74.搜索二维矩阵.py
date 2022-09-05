#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

from operator import truediv
from typing import List

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        for i in range(row):
            if target in matrix[i]:  return True
        return False
        
# @lc code=end

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
s = Solution()
print(s.searchMatrix(matrix, target))
