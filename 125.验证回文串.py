#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def __init__(self):
        self.res= {}
        self.res = {chr(item): 1 for item in range(65, 91)}
        for item in range(97, 123):
            self.res[chr(item)] = 1
        for item in range(0, 10):
            self.res[str(item)] = 1
        
    def isPalindrome(self, s: str) -> bool:
        res_s = [item.lower() for item in s if self.res.get(item, 0)]
        if not res_s:
            return True
        if len(res_s) == 1:
            return True
        start = 0
        end = len(res_s) -1
        while start <= end:
            if res_s[start] == res_s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True


# @lc code=end

s = "0P"
so = Solution()
print(so.isPalindrome(s))
