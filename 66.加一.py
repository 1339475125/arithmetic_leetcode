#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
from typing import List

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        data = digits[-1] + 1
        if data < 9:
            digits[-1] = digits[-1] + 1
            return digits
        res = self.get_data(digits)
        print(2222, res)
        return digits

    def get_data(self, digits, index=-1):
        if digits[index] + 1 <= 9:
            digits[index] += digits[index]
            return digits
        if  digits[index] + 1 > 9:
            digits[index] = 0
            
            if abs(index) >= len(digits):
                digits[0] = 0
                data = [1] + digits
                return data
            self.get_data(digits, index=index-1)
        return 
        


# @lc code=end
nums = [9,9,9]
solution = Solution()
print(solution.plusOne(nums))
