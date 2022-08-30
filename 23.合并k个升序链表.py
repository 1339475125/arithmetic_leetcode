#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#
from typing import List, Optional
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        '''合并K个有序链表（分治法）'''
        if not lists:
            return None
        n = len(lists)
        interval = 1              # 间隔
        while interval < n:     
            for i in range(0, n-interval, interval*2):
                lists[i] = self.merge2Lists(lists[i], lists[i+interval])
            interval *= 2         # 更新间隔
        return lists[0]
    
    def merge2Lists(self, l1, l2):
        '''合并两个有序链表'''
        res = cur = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        else:
            cur.next = l2
        return res.next

# @lc code=end


def build_link(nums):
    '''创建链表'''
    res = cur = ListNode(None)
    for i in nums:
        cur.next = ListNode(i)
        cur = cur.next
    return res.next

# 创建链表列表
nums_li = [[1, 4, 5], [1, 3, 4], [2, 6]]
lists = []
for i in nums_li:
    lists.append(build_link(i))

# 合并K个排序链表
s = Solution()
print(s.mergeKLists(lists))
