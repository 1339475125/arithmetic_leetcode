#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
from typing import List
# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = {}
        max_length = 0
        for num in nums:
            # 这里表示新数进来
            # 此时需要查找左右相邻的两个数对应的区间长度
            # 左右两个数的长度 + 自身的长度，就是此时新数对应的区间长度
            if num not in hash_dict:
                # 如果键不在哈希表中，取值 0
                pre_length = hash_dict.get(num - 1, 0)
                next_length = hash_dict.get(num + 1, 0)
                cur_length = pre_length + 1 + next_length
                max_length = max(max_length, cur_length)
                
                # 添加新数，同时更新两个端点的值
                # 因为序列是连续的，此时两侧端点对应的区间长度会因为当前数的加入发生改变
                hash_dict[num] = cur_length
                hash_dict[num-pre_length] = cur_length
                hash_dict[num+next_length] = cur_length

        return max_length
# @lc code=end

nums = [100, 1, 4, 3, 200, 2]
s = Solution()
print(s.longestConsecutive(nums))