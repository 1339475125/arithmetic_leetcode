#
# @lc app=leetcode.cn id=1438 lang=python3
#
# [1438] 绝对差不超过限制的最长连续子数组
#

from typing import List
# @lc code=start
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 
        stack = []
        for num in nums:
            stack.append(num)
        
# @lc code=end

