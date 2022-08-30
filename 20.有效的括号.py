#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"(": ")", "{": "}", "[": "]"}
        for item in s:
            if item == "(" or item == "{" or item == "[":
                stack.append(item)
            else:
                if not stack:
                    return False
                sign = stack.pop()
                if item  == match[sign]:
                    continue
                else:
                    return False
        return True if not stack else False
                



# @lc code=end
