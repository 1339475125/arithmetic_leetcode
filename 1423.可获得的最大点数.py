#
# @lc app=leetcode.cn id=1423 lang=python3
#
# [1423] 可获得的最大点数
# 窗口原理
#
from typing  import List
# @lc code=start
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        size = len(cardPoints)
        window = size - k
        now = sum(cardPoints[:window])

        ans = now
        for i in range(window, size):
            now += cardPoints[i] - cardPoints[i - window]
            ans = min(ans,now)
        return sum(cardPoints) - ans


# @lc code=end

cardPoints = [11,49,100,20,86,29,72]
k = 4
s = Solution()
print(s.maxScore(cardPoints, k))

