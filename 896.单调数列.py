#
# @lc app=leetcode.cn id=896 lang=python3
#
# [896] 单调数列
#

from typing import List
# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        return self.monotonic(nums)
    
    def monotonic(self, nums):
        is_increase = None
        pre_num = nums[0]
        for num in nums:
            if num - pre_num == 0:
                continue
            if is_increase is None:
                is_increase = False if num - pre_num < 0 else True
            if is_increase and num - pre_num < 0:
                return False
            if not is_increase and num - pre_num > 0:
                return False
            pre_num = num
        return True


# @lc code=end

nums = [1,1,0]
solution = Solution()
print(solution.isMonotonic(nums))

