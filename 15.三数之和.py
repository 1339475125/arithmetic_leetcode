#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
from typing import List

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort()
        N = len(nums)
        res = []
        for i in range(N-2):
            if i>0 and nums[i]==nums[i-1]:  # 优化操作，跳过重复数
                continue   # continue 是跳出当前循环，break跳出整个for循环

            target = -nums[i]
            left, right = i+1, N-1

            while left < right:
                s = nums[left] + nums[right]
                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:  # 跳过重复的要和走过的比
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1

                elif  s < target:
                    left += 1
                else:
                    right -= 1

        return res
            
# @lc code=end

