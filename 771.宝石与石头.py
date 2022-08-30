#
# @lc app=leetcode.cn id=771 lang=python3
#
# [771] 宝石与石头
#

# @lc code=start
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = {}
        sum = 0
        for item in stones:
            res[item] = res.get(item, 0) + 1
        for word in jewels:
            sum += res.get(word, 0)
        return sum

# @lc code=end

