#
# @lc app=leetcode.cn id=224 lang=python3
#
# [224] 基本计算器
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        res = 0
        num = 0
        stack = []
        sign = 1
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "+":
                res += sign * num
                num = 0
                sign = 1
            elif c == "-":
                res += sign * num
                num = 0
                sign = -1
            elif c =="(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0 
            elif c == ")":
                res += num * sign
                num = 0
                res = res * stack.pop() + stack.pop()
        res += num * sign
        return res


# @lc code=end

