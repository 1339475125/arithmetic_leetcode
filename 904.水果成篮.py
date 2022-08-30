#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] 水果成篮
#
from typing import List

# @lc code=start
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # [0, 1, 2, 2]
        # (0,1), (1, 1), (2,1), (2, 2)
        left, right = 0, 0
        fruit_type = 0
        basket = {}
        res = 0
        while right < len(fruits):  
            apple_right = fruits[right]       # 获取当前苹果
            right += 1                      # 右指针右移

            if apple_right not in basket:   # 只要出现新的苹果种类，更新一下篮子
                basket[apple_right] = 1
                fruit_type += 1
            else:                           #
                basket[apple_right] += 1

            while fruit_type > 2:
                apple_left = fruits[left]
                left += 1
                if basket[apple_left] > 0:
                    basket[apple_left] -= 1
                if basket[apple_left] == 0:
                    del basket[apple_left]
                    fruit_type -= 1

            res = max(res, right - left)
        return res

            
# @lc code=end

