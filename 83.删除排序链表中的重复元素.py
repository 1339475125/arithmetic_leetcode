#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

from typing import Optional


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        pre_val = cur.val
        while cur.next:
            if pre_val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
                pre_val = cur.val
        return head


# @lc code=end

