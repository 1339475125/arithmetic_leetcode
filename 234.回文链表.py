#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return True
        pre = head
        reverse_link = None
        while pre.next:
            node = ListNode(pre.val)
            node.next = reverse_link
            reverse_link = node
            pre = pre.next
        node = ListNode(pre.val)
        node.next = reverse_link
        reverse_link = node
        while head.next:
            head_val = head.val
            node_val = reverse_link.val
            reverse_link = reverse_link.next
            head = head.next
            if head_val != node_val:
                return False
        return True


# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    node0 = ListNode(1)
    node2 = ListNode(2)
    node0.next = node2
    node2.next =  None
    print(solution.isPalindrome(node0))