#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
from typing import List

# @lc code=start
class Solution:

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(low, high):
            if nums[low] == target == nums[high]:
                return [low, high]
            
            if nums[low] <= target <= nums[high]:
                mid = low + (high - low) // 2
                
                left = search(low, mid)
                right = search(mid+1, high)
                
                if left[0] == -1: 
                    return right
                elif right[0] == -1:
                    return left
                else:
                    return [left[0], right[1]]
            else:
                return [-1, -1]
        
        return search(0, len(nums)-1) if len(nums) > 0 else [-1, -1]

# @lc code=end

s = Solution()
nums = [5,7,7,8,8,10]
target = 8
print(s.searchRange(nums, target))
