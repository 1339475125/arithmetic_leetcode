#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
from typing import Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = slow = head
        while fast.next:
            if not fast.next.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                temp = head
                while temp != slow:
                    temp = temp.next
                    slow = slow.next
                return temp
        return None
        
# @lc code=end

