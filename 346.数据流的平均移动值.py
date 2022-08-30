# 题目描述:
# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。

# 示例:
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3


class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        from queue import Queue
        self.size = size
        self._sum = 0
        self._len = 0
        self.q = Queue(maxsize=size)

    def next(self, val: int):
        self._sum += val
        self._len += 1
        if self._len >= self.size:
            temp = self.q.get()
            self._sum -= temp
        self.q.put(val)
        return self._sum / self._len

