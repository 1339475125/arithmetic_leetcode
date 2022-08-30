#
# @lc app=leetcode.cn id=1005 lang=python3
#
# [1005] K 次取反后最大化的数组和
#
from typing import List
import copy


# @lc code=start
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        if not k:
            return sum(nums)
        sort_nums = sorted(nums)
        data = sort_nums[:k]
        pre_data = 999999
        pre_index = 0
        for index, item in enumerate(data):
            if item <= 0:
                data[index] = -item
                pre_data = -item
                pre_index = index
            elif item < pre_data:
                pre_data = -item
                pre_index = index
                data[index] = -item
            else:
                data[pre_index] = -data[pre_index]
        return sum(data+sort_nums[k:])

# @lc code=end


solution = Solution()
nums = [-2,9,9,8,4]
k = 5
print(solution.largestSumAfterKNegations(nums, k))
