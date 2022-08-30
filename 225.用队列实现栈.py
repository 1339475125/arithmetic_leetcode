#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return True if not self.stack else False



# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.stack)
obj.push(1)
print(obj.stack)
obj.push(2)
print(obj.stack)
obj.pop()
print(obj.stack)
obj.top()
print(obj.stack)
obj.empty()
print(obj.stack)
# @lc code=end

