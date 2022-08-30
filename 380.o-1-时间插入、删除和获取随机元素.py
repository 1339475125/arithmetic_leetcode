#
# @lc app=leetcode.cn id=380 lang=python3
#
# [380] O(1) 时间插入、删除和获取随机元素
#

# @lc code=start

import random

class RandomizedSet:

    def __init__(self):
        self.data = {}

    def insert(self, val: int) -> bool:
        if not self.data.get(val, None):
            self.data[val] = 1
            return True
        return False


    def remove(self, val: int) -> bool:
        if self.data.get(val, None):
            self.data.pop(val)
            return True
        return False

    def getRandom(self) -> int:
        keys = list(self.data.keys())
        size = len(self.data.keys())
        index = random.randint(0, size-1)
        key = keys[index]
        return key


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
# @lc code=end

s = RandomizedSet()
print(s.insert(1))
print(s.remove(2))
print(s.insert(2))
print(s.data)
print(s.getRandom())
print(s.remove(1))
print(s.insert(2))
print(s.getRandom())
