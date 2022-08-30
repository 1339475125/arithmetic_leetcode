#
# @lc app=leetcode.cn id=82 lang=python3
#
# [82] 删除排序链表中的重复元素 II
#

# @lc code=start
# Definition for singly-linked list.
from platform import node
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        res = {}
        cur = del_linked = pre_node = ListNode(None)
        pre_node.next = head
        while cur:
            data = res.get(cur.val, 0) + 1
            res[cur.val] = data
            cur = cur.next
        while pre_node.next:
            if res.get(pre_node.next.val, 1) > 1:
                pre_node.next = pre_node.next.next
            else:
                pre_node = pre_node.next
        return del_linked.next

# @lc code=end


if __name__ == "__main__":
    solution = Solution()
    node0 = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(4)
    node6 = ListNode(5)

    node0.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next =  None
    solution.deleteDuplicates(node0)