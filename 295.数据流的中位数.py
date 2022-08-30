#
# @lc app=leetcode.cn id=295 lang=python3
#
# [295] 数据流的中位数
#

# @lc code=start
import heapq

class MedianFinder:

    def __init__(self):
        self.len = 0
        #小顶堆
        self.minheap = []
        #大顶堆
        self.maxheap = []

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        #加入一个数，长度加1
        self.len += 1
        #首先明确的是python中的heapq是小顶堆
        #heappushpop：将num放入堆中，然后弹出并返回heap的最小元素。
        #heappush：将item的值加入heap中，保持堆的不变性。
        #heappop：弹出并返回heap的最小的元素，保持堆的不变性。
        heapq.heappush(self.maxheap, -heapq.heappushpop(self.minheap, num))
        if len(self.maxheap) > len(self.minheap):
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

    def findMedian(self):
        """
        :rtype: float
        """
        if self.len & 1 == 0:
            return (self.minheap[0] - self.maxheap[0]) / 2.0
        return self.minheap[0]

# Your MedianFinder object will be instantiated and called as such:
# @lc code=end
# obj = MedianFinder()
# obj.addNum(1)
# param_2 = obj.findMedian()
# print(param_2)
# obj.addNum(2)
# param_2 = obj.findMedian()
# print(param_2)
# obj.addNum(3)
# param_2 = obj.findMedian()
# print(param_2)
