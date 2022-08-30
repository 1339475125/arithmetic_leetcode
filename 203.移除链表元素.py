#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#

from typing import List, Optional

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return head
        cur = temp = ListNode(None)
        cur.next = head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return temp.next

# @lc code=end

