#
# @lc app=leetcode.cn id=299 lang=python3
#
# [299] 猜数字游戏
#

# @lc code=start
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        if not secret or not guess:
            return "0A0B"
        Bulls = 0  # 猜测数字中有多少位属于数字和确切位置都猜对了
        Cows = 0 # 有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）
        data_dict = {}
        for item in secret:
            data_dict[item] = data_dict.get(item, 0) + 1
        print(data_dict)
        p = 0
        q = 0
        while p < len(secret) and q < len(guess):
            if secret[p] == guess[q]:
                Bulls += 1
                if  data_dict[guess[q]] == 0:
                    Cows -= 1
                else:
                    data_dict[guess[q]] = data_dict.get(guess[q]) - 1
            elif data_dict.get(guess[q], 0):
                print(data_dict)
                Cows += 1
                data_dict[guess[q]] = data_dict.get(guess[q]) - 1
            p += 1
            q += 1
        return str(Bulls) + "A" + str(Cows) + "B"       

# @lc code=end
# "1A3B
secret = "1123"
guess = "0111"
s = Solution()
print(s.getHint(secret, guess))
