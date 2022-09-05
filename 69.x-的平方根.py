#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        low, hight = 0, x
        if  x == 1: return 1
        while low < hight:
            mid = int(low + (hight -low) // 2)
            mid_2 = mid ** 2
            if mid_2 == x:
                return mid
            if mid_2 < x and (mid +1)**2 > x:
                low = mid
                break
            if mid_2 < x:
                low = mid
            else:
                hight = mid
        return low
        
# @lc code=end
x = 36
s = Solution()
print(s.mySqrt(x))
