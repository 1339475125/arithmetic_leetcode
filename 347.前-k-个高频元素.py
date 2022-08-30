#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

from  typing import List
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data = {}
        for item in nums:
            data[item] = data.get(item, 0) + 1
        return sorted(data, key=lambda x: data[x], reverse=True)[:k]
        
# @lc code=end



nums = [1, 1, 1, 2, 3, 2]
k = 2
s = Solution()
print(s.topKFrequent(nums, k))