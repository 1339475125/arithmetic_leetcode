#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#


from typing import List


# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums
        sum_0 = 0
        sum_1 = 0
        sum_2 = 0
        for num in nums:
            if num == 0: 
                sum_0 += 1
                continue
            if num == 1:
                sum_1 += 1 
                continue
            sum_2 += 1 
        for index in range(len(nums)):
            if sum_0:
                nums[index] = 0
                sum_0 -= 1
                continue
            if sum_1:
                nums[index] = 1
                sum_1 -= 1
                continue
            nums[index] = 2
            sum_2 -= 1
        return nums



# @lc code=end

nums = [2,0,2,1,1,0]
s = Solution()
print(s.sortColors(nums))