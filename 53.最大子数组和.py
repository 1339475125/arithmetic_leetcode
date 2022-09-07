#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#
from typing import List
# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_data = nums[0]
        if len(nums) == 1:
            return max_data
        size = len(nums)
        start = 1
        while start < size:
            
# @lc code=end

