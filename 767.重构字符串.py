#
# @lc app=leetcode.cn id=767 lang=python3
#
# [767] 重构字符串
#
import collections
import heapq

# @lc code=start
class Solution:
    def reorganizeString(self, S: str) -> str:
        if len(S) < 2: return S
        dic = collections.defaultdict(int)
        for c in S:
            dic[c] += 1
        count = max(dic.values())
        if count > (len(S) + 1) // 2: return ""
        # heapq默认创建的是小根堆, 将列表初始化为一个堆, 第一个参数使用负数是使得次数较大的排列在前面也就是相当于创建的是大根堆
        queue = [(-x[1], x[0]) for x in dic.items()]
        # 将列表转化为一个小根堆
        heapq.heapify(queue)
        res = ""
        while len(queue) > 1:
            # 弹出并返回heap的最小元素
            _, letter1 = heapq.heappop(queue)
            _, letter2 = heapq.heappop(queue)
            res += letter1
            res += letter2
            # 对应字母的次数减1
            dic[letter1] -= 1
            # 对应字母的次数减1
            dic[letter2] -= 1
            if dic[letter1] > 0:
                heapq.heappush(queue, (-dic[letter1], letter1))
            if dic[letter2] > 0:
                heapq.heappush(queue, (-dic[letter2], letter2))
        # 处理字符串长度为奇数只剩下一个字符的情况
        if queue:
            res += queue[0][1]
        return res
# @lc code=end

s = "aaab"
so = Solution()
print(so.reorganizeString(s))