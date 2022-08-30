#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU 缓存
#


# @lc code=start
from datetime import datetime


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.keys = []
        self.capacity = capacity

    def get(self, key: int) -> int:
        data = self.cache.get(key, [])
        cur_datetime = datetime.now().timestamp()
        self.keys.append({key: cur_datetime})
        if data:
            data[1] = cur_datetime
            self.cache[key] = data
        return data[0] if data else -1

    def put(self, key: int, value: int) -> None:
        cur_datetime = datetime.now().timestamp()
        self.keys.append({key: cur_datetime})
        if self.cache.get(key, None):
            self.cache[key] = [value, cur_datetime]
            return 
        if len(self.cache.keys()) == self.capacity:
            while True:
                last_data = self.keys.pop(0)
                last_key = list(last_data.keys())[0]
                last_key_value = last_data.get(last_key)
                if self.cache.get(last_key, None) and self.cache.get(last_key)[1] <= last_key_value:
                    self.cache.pop(last_key)
                    break
        self.cache[key] = [value, cur_datetime]
        return
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end
# [null,null,null,1,null,-1,null,-1,3,4]
l =LRUCache(capacity=2)
print(l.put(1, 1))
print(l.put(2, 2))
print(l.get(1))
print(l.put(3, 3))
print(l.get(2))
print(l.put(4, 4))
print(l.get(1))
print(l.get(3))
print(l.get(4))

