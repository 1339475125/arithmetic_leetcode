#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        size = len(s)
        count = size
        step = 2
        while step <= size:
            start = 0
            while start < size - step +1:
                if self.istPalindrome(s[start:start+step]):
                    count += 1
                start += 1
            step += 1
        return count

    def istPalindrome(self, data):
        start = 0
        end = len(data) -1
        while start <= end:
            if data[start] == data[end]:
                start += 1
                end -= 1
            else:
                return False
        return True



# @lc code=end
s = "aaa"
so = Solution()
print(so.countSubstrings(s))

