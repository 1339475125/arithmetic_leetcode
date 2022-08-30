#
# @lc app=leetcode.cn id=692 lang=python3
#
# [692] 前K个高频单词
#
from typing import List

# @lc code=start
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        if not words or not k:
            return []
        res = []
        frequent_cnt_dict = {}
        for word in words:
            frequent_cnt_dict[word] = frequent_cnt_dict.get(word, 0) + 1
        
        data = sorted(frequent_cnt_dict.items(), key=lambda kv:(-kv[1], kv[0]))
        for i in range(k):
            res.append(data[i][0])
        return res


# @lc code=end

