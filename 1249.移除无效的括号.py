#
# @lc app=leetcode.cn id=1249 lang=python3
#
# [1249] 移除无效的括号
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        for i, v in enumerate(s):
            if v == ')':
                if st and st[-1][0] == '(':
                    st.pop()
                    continue
                st.append([v, i])
            elif v == '(':
                st.append([v, i])
        
        res, t = "", 0
        for i, v in enumerate(s):
            if t < len(st) and i == st[t][1]:
                t += 1
                continue
            res += v
        return res

# @lc code=end
s = "))(("
so = Solution()
print(so.minRemoveToMakeValid(s))

