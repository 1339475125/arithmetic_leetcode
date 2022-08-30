#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

from typing import List
# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        stack_in = []
        for item in tokens:
            if item not in ("+", "-", "*", "/"):
                stack_in.append(item)
            else:
                temp = []
                temp.append(stack_in.pop(-1))
                temp.append(stack_in.pop(-1))
                if item == "*":
                    data = int(temp[-1]) * int(temp[0])
                if item == "+":
                    data = int(temp[-1]) + int(temp[0])
                if item == "-":
                    data = int(temp[-1]) - int(temp[0])
                if item == "/":
                    if int(temp[0]) == 0:
                        return None
                    data = int(int(temp[-1]) / int(temp[0]))
                stack_in.append(data)
        return stack_in[0]
# @lc code=end


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
s = Solution()
print(s.evalRPN(tokens))
