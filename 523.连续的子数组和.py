#
# @lc app=leetcode.cn id=523 lang=python3
#
# c
#

from typing import List


# @lc code=start
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return '00' in ''.join(map(str, nums))
        pre_sum = {0:-1}
        cur_sum = 0
        for i, num in enumerate(nums):
            cur_sum = (num + cur_sum) % k
            if cur_sum in pre_sum and i - pre_sum[cur_sum] > 1:               
                return True
            if cur_sum not in pre_sum:
                pre_sum[cur_sum] = i
        return False

# @lc code=end
nums = [23,2,4,6,7]
k = 6
s = Solution()
print(s.checkSubarraySum(nums, k))
data = [[23,2,4,6,7], [25, 6, 10, 9], [29, 12, 17]]