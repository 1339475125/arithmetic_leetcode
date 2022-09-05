#
# @lc app=leetcode.cn id=1095 lang=python3
#
# [1095] 山脉数组中查找目标值
#

# @lc code=start
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """

class MountainArray:
   def get(self, index: int) -> int:
       pass
   def length(self) -> int:
       pass

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left = 0
        right = MountainArray.length()

        while left <= right:
            mid  = left + (right - left ) // 2
            mid_data = MountainArray.get(mid)
            mid_1_data = MountainArray.get(mid + 1)
            if mid_data == target:
                return mid
            if mid_data > target:
                if mid_data < mid_1_data:
                    right = mid
                else:
                    left = mid + 1
            else:
                if mid_data < mid_1_data:
                    right = mid
                else:
                    left = mid + 1
        return  -1
# @lc code=end

