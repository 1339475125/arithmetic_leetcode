#
# @lc app=leetcode.cn id=179 lang=python3
#
# [179] 最大数
#

from typing import List


# @lc code=start
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


# @lc code=end

