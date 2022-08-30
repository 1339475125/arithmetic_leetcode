#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from typing import Optional
from utils.linked import create_link_from_list

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        prev = None
        curr = head
        while curr:
            last = curr.next
            curr.next= prev
            prev = curr
            curr = last
        return prev
        
# @lc code=end
values = [1,2,3,4,5]
head = create_link_from_list(values)
s = Solution()
print(s.reverseList(head))

