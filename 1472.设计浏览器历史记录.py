#
# @lc app=leetcode.cn id=1472 lang=python3
#
# [1472] 设计浏览器历史记录
#

# @lc code=start
class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = [homepage]
        self.in_stack = [homepage]

    def visit(self, url: str) -> None:
        print()
        self.back_stack.append(url)

    def back(self, steps: int) -> str:
        print(self.back_stack)
        for i in range(steps):
            if not self.back_stack:
                return None
            data = self.back_stack.pop(-1)
            self.in_stack.append(data)
        return data

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if not self.in_stack:
                return None
            data = self.in_stack.pop(-1)
            self.back_stack.append(data)
        return data


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# @lc code=end

