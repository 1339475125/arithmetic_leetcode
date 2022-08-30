#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
from typing import List
# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals
        # 排序， 按照p[0]排序
        self.quick_sort_between(intervals, 0, len(intervals)-1)
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][1]:
                res[-1] = [res[-1][0], max(res[-1][1], interval[1])]
            else:
                res.append(interval)
        return res

    def partition(self, arr: List[int], low: int, high: int):
        pivot, j = arr[low][0], low
        for i in range(low + 1, high + 1):
            if arr[i][0] <= pivot:
                j += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[low], arr[j] = arr[j], arr[low]
        return j 

    def quick_sort_between(self, arr: List[int], low: int, high: int):
        if high-low < 1: # 递归结束条件
            return
        m = self.partition(arr, low, high)  # arr[m] 作为划分标准
        self.quick_sort_between(arr, low, m - 1)
        self.quick_sort_between(arr, m + 1, high)


# @lc code=end

intervals = [[1,4],[0,2],[3,5]]
s = Solution()
print(s.merge(intervals))