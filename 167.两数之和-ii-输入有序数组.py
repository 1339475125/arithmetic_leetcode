#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#
from typing import List

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        size  = len(numbers)
        start  = 1
        pre_data = None
        while start < size:
            end = size -1
            if pre_data == numbers[start -1]:
                start +=1
                continue
            pre_data = numbers[start -1]
            temp = target - numbers[start -1]
            while start -1 < end:
                if numbers[end] == temp:
                    return [start, end +1]
                end -= 1
            start +=1
        return [start, end+1]
      
        
# @lc code=end
numbers = [12,13,23,28,43,44,59,60,61,68,70,86,88,92,124,125,136,168,173,173,180,199,212,221,227,230,277,282,306,314,316,321,325,328,336,337,363,365,368,370,370,371,375,384,387,394,400,404,414,422,422,427,430,435,457,493,506,527,531,538,541,546,568,583,585,587,650,652,677,691,730,737,740,751,755,764,778,783,785,789,794,803,809,815,847,858,863,863,874,887,896,916,920,926,927,930,933,957,981,997]
target = 542
s = Solution()
print(s.twoSum(numbers, target))