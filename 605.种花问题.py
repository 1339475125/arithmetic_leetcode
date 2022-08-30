#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#
from typing import List

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # [0, 0, 0, 1, 0, 1]
        for i, x in enumerate(flowerbed):
            if not x: # 空地
                if (i - 1 < 0 or flowerbed[i - 1] == 0) and (i + 1 == len(flowerbed) or flowerbed[i + 1] == 0): # 不冲突
                    flowerbed[i] = 1
                    n -= 1
 
        return n <= 0
        # @lc code=end

# a = [1,0,0,0,0,1]
# n = 2
# solution = Solution()
# print(solution.canPlaceFlowers(a, n))