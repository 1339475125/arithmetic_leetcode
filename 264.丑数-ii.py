#
# @lc app=leetcode.cn id=264 lang=python3
#
# [264] 丑数 II
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        res = [1]
        a, b , c = 0, 0, 0
        for x in range(1, n):
            k = min(res[a]*2,res[b]*3,res[c]*5)
            res.append(k)
            if res[x]==res[a]*2:
                a+=1
            if res[x]==res[b]*3:
                b+=1
            if res[x]==res[c]*5:
                c+=1
        return res[n-1]

        
# @lc code=end

