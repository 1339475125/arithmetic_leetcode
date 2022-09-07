#
# @lc app=leetcode.cn id=1031 lang=python3
#
# [1031] 两个非重叠子数组的最大和
# 窗口
#
from typing import List
# @lc code=start
class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        if secondLen > firstLen:
            return self.maxSumTwoNoOverlap(nums, secondLen, firstLen)
        first_max_sum, first_index_data = self.window_max_sum_num(nums, firstLen)
        scend_max_sum, second_index_data = self.window_max_sum_num(nums, secondLen)
        print(first_index_data, second_index_data)
        if (
                first_index_data[-1][0] <= second_index_data[-1][0] and first_index_data[-1][1] >= second_index_data[-1][1] or 
                first_index_data[-1][0] > second_index_data[-1][0] and first_index_data[-1][1] < second_index_data[-1][1]
                ):
            return sum(max(
                nums[first_index_data[-1][0]:first_index_data[-1][1]] + nums[second_index_data[-2][0]:first_index_data[-2][1]],
                nums[first_index_data[-2][0]:first_index_data[-2][1]] + nums[second_index_data[-1][0]:first_index_data[-1][1]]
            ))
        return first_max_sum + scend_max_sum
        
    def window_max_sum_num(self,  nums: List[int], window_size: int):
        size = len(nums)
        max_data = 0
        res = []
        for i in range(size - window_size):
            data = nums[i:i+window_size]
            if sum(data) > max_data:
                res.append([i, i+window_size])
            max_data = max(max_data, sum(data))
        return max_data, res
        
# @lc code=end
A = [2,1,5,6,0,9,5,0,3,8]
L = 4
M = 3
s = Solution()
print(s.maxSumTwoNoOverlap(A, L, M))
