#
# @lc app=leetcode.cn id=735 lang=python3
#
# 
#
from typing import List

# @lc code=start
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) == 2 and sum(asteroids) == 0:
            return []
        res = []
        for item in asteroids[::-1]:
            if not res:
                res.append(item)
                continue
            if item >0 and res[-1] == -item:
                res.pop(-1)
                continue
            if res[-1] * item  < 0:
                if item < 0:
                    res.append(item)
                elif abs(item) > abs(res[-1]):
                    res.pop(-1)
                    res.append(item)
                continue
            if res[-1] * item  >= 0:
                res.append(item)
                continue
        return res[::-1]
                    

# @lc code=end
asteroids = [-2,2,-1,-2]
s = Solution()
print(s.asteroidCollision(asteroids))
