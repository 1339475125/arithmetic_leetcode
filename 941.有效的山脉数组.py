#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

from typing import List

from sqlalchemy import true

# @lc code=start
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        # 定义指针
        left = 0
        right = n - 1

        # 先处理 left 指针
        # 满足右边的值大于当前值时，往右移动
        # 注意边界
        while left + 1 < n and arr[left] < arr[left+1]:
            left += 1
        # 处理 right 指针
        # 满足左边的值大于当前值时，往左移动，同样注意边界问题
        while right - 1 > 0 and arr[right - 1] > arr[right]:
            right -= 1
        # 判断 left 指针是否与 right 指针重合
        # 同时注意，峰顶不能在数组两端
        if left > 0 and right < n - 1 and left == right:
            return True
        
        return False

# @lc code=end

arr = [0,1,2,1,2]
solution = Solution()
print(solution.validMountainArray(arr))

