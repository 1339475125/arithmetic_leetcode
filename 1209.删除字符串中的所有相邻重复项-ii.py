#
# @lc app=leetcode.cn id=1209 lang=python3
#
# [1209] 删除字符串中的所有相邻重复项 II
#

# @lc code=start


class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        a,b,result = [],[],""
        for i in range(len(s)):
            if a == [] or a[-1] != s[i]:
                a.append(s[i])
                b.append(1)
            elif b[-1] < k:
                b[-1] += 1
            if b[-1] == k:
                a.pop()
                b.pop()
        for i in range(len(a)):
            result += a[i] * b [i]
        return result

        # @lc code=end

s = "deeedbbcccbdaa"
k = 3
so = Solution()
print(so.removeDuplicates(s, k))

