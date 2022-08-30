#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#
import json
from typing import List

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            key = ''.join(sorted(str))
            if key in dic:
                dic[key].append(str)
            else:
                dic[key] = [str]
        return list(dic.values())
                
            

        
# @lc code=end

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
print(s.groupAnagrams(strs))
