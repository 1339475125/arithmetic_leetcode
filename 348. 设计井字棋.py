#
# @lc app=leetcode.cn id=20 lang=python3
#
# [348] 设计井字棋
#

# @lc code=start


class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[row] += player
        self.cols[col] += player
        if self.is_win():
            return True
        return False
    
    def is_win(self):
        


# @lc code=end


s = TicTacToe(3)
s.move(0, 0, 1)