#
# @lc app=leetcode.cn id=2194 lang=python3
#
# [2194] Excel 表中某个范围内的单元格
#
from typing import List
import statsd

# @lc code=start
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        strs = [
            "A",
            "B",
            "C",
            "D",
            "E",
            "F",
            "G",
            "H",
            "I",
            "J",
            "K",
            "L",
            "M",
            "N",
            "O",
            "P",
            "Q",
            "R",
            "S",
            "T",
            "U",
            "V",
            "W",
            "X",
            "Y",
            "Z"
        ]
        res = []
        datas = s.split(":")
        start_str = ord(datas[0][: -1]) -65
        start_index = int(datas[0][-1])
        end_str = ord(datas[1][: -1]) -65
        end_index = int(datas[1][-1])
        for item in strs[start_str: end_str+1]:
            for i in range(start_index, end_index+1):
                res.append(f"{item}{i}")
        return res


# @lc code=end

if __name__ == "__main__":
    solution = Solution()
    s = "K1:L2"
    print(solution.cellsInRange(s))
