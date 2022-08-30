#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#


from typing import List


# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if len(nums) == 1 and k == 1:
            return nums[0]
        if k >= len(nums):
            return None
        # 快速排序
        self.quickSort(nums, 0, len(nums) -1)
        print(nums)
        return nums[-k]
        

    def partition(self, nums, low, high):
        pivot, j = nums[0], low
        for i in range(low + 1, high + 1):
            if nums[i] <= pivot:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]
        nums[low], nums[j] = nums[j], nums[low]
        return j


    def quickSort(self, nums: List[int], low: int, high: int):
        if high-low < 1: # 递归结束条件
            return
        m = self.partition(nums, low, high)  # arr[m] 作为划分标准
        self.quickSort(nums, low, m - 1)
        self.quickSort(nums, m + 1, high)


        
          
# @lc code=end
nums = [3,2,1,5,6,4]
k = 2
s = Solution()
print(s.findKthLargest(nums, k))
