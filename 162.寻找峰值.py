#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#
from typing import List

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        start = 0
        end = len(nums) - 1
 
        while(start <= end):
            mid = start + (end - start) // 2
 
            if(mid+1 > end):
                return mid
            if(nums[mid] < nums[mid+1]):
                start = mid + 1
            else:
                end = mid
        return mid
        
# @lc code=end
nums = [1]
s =Solution()
print(s.findPeakElement(nums))
