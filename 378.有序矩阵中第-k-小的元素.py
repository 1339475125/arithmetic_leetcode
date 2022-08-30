#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第 K 小的元素
#
from typing import List
# @lc code=start
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # if not matrix:
        #     return matrix
        # if len(matrix) == 1 and len(matrix[0]) == 1 and k == 1:
        #     return matrix[0][0]
        # res = []
        # for row in matrix:
        #     for ele in row:
        #         res.append(ele)
        # res.sort()
        # return res[k-1]
                
        def search(mid, n):
            # 从左下角开始往右上角找
            i, j = n-1, 0
            # 统计小于或等于 mid 的元素个数
            count = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    # 当此时元素小于等于 mid
                    # 那么该元素往上的所有元素都会小于或等于 mid
                    count += (i + 1)
                    # 向右移动，继续比较
                    j += 1
                else:
                    # 当此时元素大于 mid 时，说明这个元素不包含在内，往上移动
                    i -= 1
            # count 与 k 值比对，判断所求元素落在哪边
            return count >= k
        
        n = len(matrix)

        left, right = matrix[0][0], matrix[n-1][n-1]

        while left < right:
            mid = left + (right - left) // 2
            if search(mid, n):
                # 当 count 大于等于 k 时，表明答案落在 [left, mid]
                # 否则落在 [mid+1, right]
                right = mid
            else:
                left = mid + 1
        
        return left

# @lc code=end

