#
# @lc app=leetcode.cn id=895 lang=python3
#
# [895] 最大频率栈
#

# @lc code=start

class FreqStack:

    def __init__(self):
        self.res = {}
        self.group = {}
        self.max_freq = None

    def push(self, val: int) -> None:
        self.res[val] = self.res.get(val, 0) + 1
        1 if not self.max_freq else max(self.res[val], self.max_freq)
        self.group[self.res[val]] = self.group.get(self.res[val], []).append(val)
        return

    def pop(self) -> int:
        groups = self.group.get(self.max_freq)
        if not groups:
            self.max_freq -= 1
            if not self.max_freq:
                return 0
        max_val = groups.pop(0)
        return max_val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
# @lc code=end

