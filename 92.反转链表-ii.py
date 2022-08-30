#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from typing import Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        right = right -1
        left = left -1

        while( right-left>=0 ):
            # 左侧节点
            l = head
            for i in range(left):
                l = l.next
            # 右侧节点
            r = head
            for i in range(right):
                r = r.next
            # print(l.val, r.val)
            l.val, r.val = r.val, l.val
            right = right-1
            left = left+1
        return head


# @lc code=end

