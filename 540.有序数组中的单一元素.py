#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#
from  typing import List


# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        res = nums[0]
        for num in nums[1:]:
            res = res ^ num
        return res

# @lc code=end

