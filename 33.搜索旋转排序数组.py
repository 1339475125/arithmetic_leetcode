#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def searcNum(left, right):
            while left <= right:
                mid = left + (right - left)  // 2
                if nums[mid] == target:
                    return mid
                if nums[mid] < nums[right]:
                    if target <= nums[right] and nums[mid] < target:
                        left = mid+1
                    else:
                        right = mid
                else:
                    if target >= nums[left] and nums[mid] > target:
                        right = mid
                    else:
                        left=mid+1
            return -1
        return -1 if not nums else searcNum(0, len(nums)-1)


# @lc code=end

nums = [4,5,6,7,0,1,2]
target = 0
s = Solution()
print(s.search(nums, target))