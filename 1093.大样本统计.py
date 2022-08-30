#
# @lc app=leetcode.cn id=1093 lang=python3
#
# [1093] 大样本统计
#

# @lc code=start
from typing import List

class Solution:
    def sampleStats(self, count: List[int]) -> List[float]:
        if not count:
            return [0, 0, 0, 0, 0]

        minimum = min(count)
        maximum = max(count)
        mean = sum(count) / count(count)
        median = mid(count)
        mode = 

# @lc code=end

