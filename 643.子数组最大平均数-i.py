#
# @lc app=leetcode.cn id=643 lang=python3
#
# [643] 子数组最大平均数 I
#
from  typing import List

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or not k:
            return 0

        if len(nums) < k:
            return 0
        
        if len(nums) == k:
            return sum(nums) / len(nums)
        pre = sum(nums[:k])
        max_data = pre
        for i in range(1, len(nums) -k + 1):
            data = pre - nums[i-1] + nums[i+k-1]
            pre = data
            max_data = max(max_data, data)
        return max_data / k
# @lc code=end
nums = [1, 2]
k = 4
solution = Solution()
print(solution.findMaxAverage(nums, k))

