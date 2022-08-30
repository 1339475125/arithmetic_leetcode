#
# @lc app=leetcode.cn id=350 lang=python3
#
# [350] 两个数组的交集 II
#
from typing import List
# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        if not nums1 or not nums2:
            return []
        data = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] > nums2[index2]:
                index2 += 1
            elif nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                data.append(nums1[index1])
                index1 += 1
                index2 += 1
        return data
            
# @lc code=end
nums1 = [3,1,2]
nums2 = [1, 3]
s = Solution()
print(s.intersect(nums1, nums2))

