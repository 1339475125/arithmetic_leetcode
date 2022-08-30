#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#

from typing import List
# @lc code=start
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return  max(nums)
        set_nums = list(set(nums))
        if len(set_nums) < 3:
            return max(set_nums)
        return sorted(set_nums, reverse=True)[2]
# @lc code=end

