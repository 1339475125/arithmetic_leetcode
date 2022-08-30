#
# @lc app=leetcode.cn id=925 lang=python3
#
# [925] 长按键入
#

# @lc code=start
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed or len(name) > len(typed):
            return False
        if len(name) == len(typed):
            return True if name == typed else False
        pre_word = ""
        start_j = 0
        for i in range(len(name)):
            for j in range(start_j, len(typed)):
                if name[i] == typed[j]:
                   pre_word = name[i]
                   start_j += 1
                   break
                elif typed[j] == pre_word:
                    start_j += 1
                    continue
                else:
                    return False
        if start_j < len(typed): 
            if len(list(set(typed[start_j:]))) == 1 and list(set(typed[start_j:]))[0]==pre_word:
                return True
            return False
        return True
# @lc code=end



if __name__ == "__main__":
    name = "pyplrz"
    typed = "ppyypllr"
    solution = Solution()
    solution.isLongPressedName()