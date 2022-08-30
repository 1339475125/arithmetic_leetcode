#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

from typing import Optional
from urllib.parse import non_hierarchical


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA and not headB:
            return None
        pA, pB = headA, headB
        while pA != pB:
            pA  = pB if not pA  else pA.next
            pB = pA if not pB  else pB.next
        return pA

        
# @lc code=end

