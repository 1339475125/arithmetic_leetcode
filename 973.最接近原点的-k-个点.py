#
# @lc app=leetcode.cn id=973 lang=python3
#
# [973] 最接近原点的 K 个点
#
from  typing  import List
from heapq import *
# @lc code=start
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        distance = []
        heapify(distance)
        for index, (i, j) in enumerate(points):
            heappush(distance, (i ** 2 + j ** 2, index))
        res = []
        while K:
            K -= 1
            _, idx = heappop(distance)
            res.append(points[idx])
            
        return res


# @lc code=end
points = [[6,10],[-3,3],[-2,5],[0,2]]
k = 3
s = Solution()
print(s.kClosest(points, k))